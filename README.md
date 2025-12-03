# Data Engineering Challenge

## 🏢 The Client Scenario
Your client is a large retail company. They are currently struggling to reconcile their **Sales** data with their **Rebates** data. The Head of Sales is concerned about data quality and needs a reliable view of performance.

They have provided two raw datasets but are unable to match them up accurately to calculate the true net revenue per region.

## 🎯 The Objective
You have been asked to deliver a Proof of Concept (POC) pipeline. 
Your goal is to demonstrate **Databricks Data Engineering best practices** to turn raw files into a reliable data product.

You must:
1.  **Ingest** the raw sales and rebate data from the cloud.
2.  **Process** the data to handle quality issues and reconcile the datasets.
3.  **Model** the final output for business consumption (e.g., a Star Schema or Dimensional Model).
4.  **Analyze** the data to generate key insights.
5.  **Present** the key findings back to the Head of Sales.

## 🛠️ Technical Requirements
* **Language:** Python / PySpark.
* **Storage:** Delta Lake.
* **Format:** You may use Python Scripts (`.py`) or Jupyter Notebooks (`.ipynb`).
* **Architecture:** We expect you to design a medallion architecture that reflects industry standards for scalability and data quality.

## 📂 The Data
The raw data is hosted in **Azure Blob Storage**. To access it, you must use the **Azure Blob Storage SDK** for Python (pre-installed in this environment).

**⚠️ Important Workflow Note:**
This environment is designed for a **two-step ingestion process**:
1.  **Download:** Write a standard Python script to authenticate with Azure and download the raw CSV files to your local Codespace storage (e.g., `src/data/raw/`).
2.  **Process:** Use PySpark to read the downloaded local files and write them to your Delta Lake Bronze layer.

### Connection Details
* **Account Name:** `sttiliedatachallenge`
* **Container Name:** `til-ie-data-challenge`
* **SAS Token:** The shared access token will have been provided by email.
   *(Note: This token provides Read and List permissions only)*
* **File Structure:** The container has two virtual folders: `sales/` and `rebates/`.

## 📝 Deliverables
You have full autonomy over the project structure. Your submission must include:

### 1. Ingestion Script
A Python script (using `azure-storage-blob`) that connects to the cloud container, lists the files, and downloads them to your local environment.

### 2. The Pipeline Code (`src/`)
A PySpark pipeline that takes the data from the local raw folder to final analytical tables. 

### 3. Analysis Script/Notebook
A script or notebook that queries your final data model to find:
* Total Sales vs. Total Rebates by Region.
* Top Performing Sales Reps.
* Any other interesting insights you can identify.
* Any data quality issues found.

### 4. Presentation
A PDF or Slide Deck (Max 5 slides) addressed to the **Head of Sales**.
* Summarize key insights.
* Highlight data quality issues encountered.
* Explain your architectural choices and why you chose them.
* How could the POC be improved upon? How would you further develop the solution if given more time?

## 🚀 How to Start the Challenge
1.  Create a repository using the **[til-ie-data-challenge-template](https://github.com/TIL-HC/til-ie-data-challenge-template)**.
2.  Name the repository **til-ie-data-challenge-[first name]-[last name]** and make sure it's **private**.
3.  Click the **Code** button (green) in GitHub.
4.  Select the **Codespaces** tab.
5.  Click **Create codespace on main**.
6.  Wait for the environment to build (approx. 2 mins).
7.  **Step 1:** Write your Azure download script.
8.  **Step 2:** Build your Spark solution.

### 💻 Using Terminal
You can also run standard python scripts in the terminal:
```bash
python src/your_script_name.py

### 📓 Using Jupyter Notebooks
If you prefer to work in Notebooks:
1.  Create a file with the `.ipynb` extension inside the `src/` folder.
2.  When you run the first cell, VS Code will ask you to **Select Kernel**.
3.  Choose **Python Environments...** -> **Python 3.10.x**.
