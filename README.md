# Retail Analytics Platform

## Overview

The Retail Analytics Platform is an end-to-end Data Engineering project built using Azure, Python, Snowflake, dbt, Airflow, and SQL. The platform ingests retail sales, customer, product, and inventory data from multiple sources, processes and transforms the data using modern data engineering practices, and delivers curated datasets for business analytics and reporting.

The project follows the Medallion Architecture (Bronze, Silver, Gold) and implements automated ETL pipelines, data quality checks, orchestration workflows, and dimensional data modeling.

---

## Business Problem

Retail organizations generate large volumes of transactional and operational data across multiple systems. Business stakeholders require a centralized analytics platform to answer questions such as:

- What are the daily, weekly, and monthly sales trends?
- Which products generate the highest revenue?
- Which customers contribute most to revenue?
- Which stores are performing best?
- Which products are low in stock and require replenishment?

This platform solves these challenges by creating a scalable data pipeline that transforms raw retail data into business-ready datasets.

---

## Architecture

```text
Source Systems
│
├── Sales Data (CSV)
├── Customers Data (CSV)
├── Products Data (CSV)
├── Inventory Data (CSV)
│
▼
Azure Data Lake Storage Gen2
(Bronze Layer)
│
▼
Python Data Validation & Ingestion
│
▼
Snowflake RAW Schema
│
▼
dbt Transformations
│
├── Staging Layer
├── Intermediate Layer
└── Mart Layer
│
▼
Snowflake Analytics Tables
│
▼
Power BI Dashboards
│
▲
│
Apache Airflow Orchestration
```

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Ingestion & Validation |
| SQL | Data Transformation |
| Azure Data Lake Storage Gen2 | Data Lake |
| Snowflake | Cloud Data Warehouse |
| dbt | Data Transformation & Testing |
| Apache Airflow | Workflow Orchestration |
| Power BI | Reporting & Visualization |
| GitHub | Version Control |
| GitHub Actions | CI/CD |

---

## Project Structure

```text
retail-analytics-platform/
│
├── airflow/
│   └── dags/
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│
├── data/
│   ├── customers/
│   ├── products/
│   ├── sales/
│   └── inventory/
│
├── scripts/
│   ├── ingestion/
│   ├── validation/
│   └── snowflake_load/
│
├── sql/
│
├── dashboards/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

## Data Pipeline Flow

### 1. Data Ingestion

Retail datasets are received as CSV files and stored in Azure Data Lake Storage Gen2 Bronze layer.

Datasets include:

- Customers
- Products
- Stores
- Sales Transactions
- Inventory

---

###