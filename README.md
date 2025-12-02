# Retail Data Engineering Challenge

## 🏢 The Client Scenario
Your client is a large retail company. They are currently struggling to reconcile their **Sales** data with their **Rebates** data. The Head of Sales is concerned about data quality and needs a reliable view of performance.

They have provided two raw datasets but are unable to match them up accurately to calculate the true net revenue per region.

## 🎯 The Objective
You have been asked to deliver a Proof of Concept (POC) pipeline. 
Your goal is to demonstrate **Databricks Data Engineering best practices** to turn raw files into a reliable data product.

You must:
1.  **Ingest** the raw sales and rebate data.
2.  **Process** the data to handle quality issues and reconcile the datasets.
3.  **Model** the final output for business consumption (e.g., a Star Schema or Dimensional Model).
4.  **Analyze** the data to generate key insights.

## 🛠️ Technical Requirements
* **Language:** Python / PySpark.
* **Storage:** Delta Lake.
* **Format:** You may use Python Scripts (`.py`) or Jupyter Notebooks (`.ipynb`).
* **Architecture:** We expect you to design a pipeline architecture that reflects industry standards for scalability and data quality.

## 📂 The Data
The data is hosted at the following URL:
* **URL:** [INSERT_YOUR_S3_URL_HERE]
* **Format:** CSV (Header included)
* **Files included:** `sales_transactions.csv`, `rebate_transactions.csv`

## 📝 Deliverables
You have full autonomy over the project structure. Your submission must include:

### 1. The Pipeline Code (`src/`)
A PySpark pipeline that takes the data from raw source to final analytical tables. 

### 2. Analysis Script/Notebook
A script or notebook that queries your final data model to answer:
* Total Sales vs. Total Rebates by Region.
* Top Performing Sales Reps.
* Any data quality issues found (e.g., How many rebates could not be matched to a sale?).

### 3. Presentation
A PDF or Slide Deck (Max 5 slides) addressed to the **Head of Sales**.
* Summarize key insights.
* Highlight data quality issues encountered.
* Explain your architectural choices and why you chose them.

## 🚀 How to Start the Challenge
1.  Create a repository using the **til-ie-data-challenge-template**.
2.  Name the repository **til-ie-data-challenge-[first name]-[last name]**.
3.  Click the **Code** button (green) in GitHub.
4.  Select the **Codespaces** tab.
5.  Click **Create codespace on main**.
6.  Wait for the environment to build (approx. 2 mins).

### 📓 Using Jupyter Notebooks
If you prefer to work in Notebooks:
1.  Create a file with the `.ipynb` extension inside the `src/` folder.
2.  When you run the first cell, VS Code will ask you to **Select Kernel**.
3.  Choose **Python Environments...** -> **Python 3.10.x**.

### 💻 Using Terminal
You can also run standard python scripts in the terminal:
```bash
python src/your_script_name.py
