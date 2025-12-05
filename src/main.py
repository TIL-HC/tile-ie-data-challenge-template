"""Orchestrator for the POC pipeline.

This script can optionally download raw CSVs from Azure Blob Storage (using
the SAS token) and then runs the PySpark Delta steps: bronze -> silver ->
gold. It creates one SparkSession (with Delta enabled) and reuses it across
the steps.
"""
from pathlib import Path
import logging
import argparse
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
import os


from src.ingestion.azure_download import download_container_csvs
from src.bronze.bronze_delta import write_bronze
from src.transformations.silver_delta import build_silver
from src.modeling.gold_delta import build_gold


def create_spark(app_name: str = 'til_poc_pipeline') -> SparkSession:
    builder = SparkSession.builder.appName(app_name)
    builder = builder.config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension')
    builder = builder.config('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog')
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark


def run_full_pipeline(base: str, account: str = None, container: str = None, sas: str = None, do_azure: bool = False):
    base_p = Path(base)
    raw = base_p / 'data' / 'raw'
    bronze = base_p / 'data' / 'bronze'
    silver = base_p / 'data' / 'silver'
    gold = base_p / 'data' / 'gold'

    logging.info('Starting POC pipeline')

    if do_azure:
        # If flags are missing, attempt to load from environment or .env file
        if not (account and container and sas):
            # First try environment variables
            account = account or os.getenv('ACCOUNT_NAME')
            container = container or os.getenv('CONTAINER_NAME')
            sas = sas or os.getenv('AZURE_SAS_TOKEN')
            # If still missing, try to load .env from repo root
            if not (account and container and sas):
                env_path = Path('.') / '.env'
                if env_path.exists():
                    for line in env_path.read_text().splitlines():
                        if not line or line.strip().startswith('#'):
                            continue
                        if '=' not in line:
                            continue
                        k, v = line.split('=', 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k == 'ACCOUNT_NAME' and not account:
                            account = v
                        if k == 'CONTAINER_NAME' and not container:
                            container = v
                        if k == 'AZURE_SAS_TOKEN' and not sas:
                            sas = v
        if not (account and container and sas):
            raise ValueError('To run Azure download provide --account, --container and --sas (or set them in the environment or .env)')
        logging.info('Downloading raw CSVs from Azure Blob Storage')
        n = download_container_csvs(account, container, sas, str(raw))
        logging.info(f'Downloaded {n} files into {raw}')
    else:
        logging.info('Skipping Azure download; using local files in %s', raw)

    spark = create_spark()

    logging.info('Running Bronze ingestion (CSV -> Delta)')
    write_bronze(spark, str(raw), str(bronze))

    logging.info('Running Silver transformations and reconciliation')
    build_silver(spark, str(bronze), str(silver))

    logging.info('Running Gold modeling to create dims and fact')
    build_gold(spark, str(silver), str(gold))

    logging.info('Pipeline complete. Gold tables available in %s', gold)
    spark.stop()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Run the til IE POC pipeline')
    parser.add_argument('--base', default='.', help='Project base directory')
    parser.add_argument('--azure', action='store_true', dest='do_azure', help='Download from Azure Blob before processing')
    parser.add_argument('--account', help='Azure storage account name')
    parser.add_argument('--container', help='Azure container name')
    parser.add_argument('--sas', help='SAS token (include leading ? )')
    args = parser.parse_args()

    run_full_pipeline(args.base, account=args.account, container=args.container, sas=args.sas, do_azure=args.do_azure)
