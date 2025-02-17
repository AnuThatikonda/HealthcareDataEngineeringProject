# Health Data Engineering

This project is focused on building a data engineering pipeline for healthcare data analysis. The pipeline encompasses data ingestion, cleaning, transformation, warehousing, and analysis using AWS technologies. The goal of the project is to create an ETL pipeline that processes and analyzes healthcare-related data, providing insights into patient admissions, hospital performance, and medical conditions.

## Project Overview

### Steps Followed:

1. **Data Ingestion (AWS S3)**
   - **Data Storage**: The dataset was ingested and stored in an AWS S3 bucket in CSV format.
   - **ETL Pipeline Initiation**: Used **AWS Lambda** to trigger the data transformation process upon new file uploads to the S3 bucket.

2. **Data Cleaning & Transformation (AWS Lambda & Python)**
   - **Data Cleaning**: The data was cleaned using **AWS Lambda** functions to standardize values and fix inconsistencies.
     - Inconsistent name capitalizations (e.g., "Bobby JacksOn" → "Bobby Jackson") were corrected.
     - Gender values were standardized to consistent terms (e.g., "Male", "Female").
     - Medical conditions and blood types were validated and standardized.
   - **Date Transformation**: Dates such as `Date of Admission` and `Discharge Date` were converted to the proper date format.
   - **Handling Missing Data**: Managed missing values in `Test Results` and `Medication` columns and ensured the integrity of the dataset.
   - **Billing Amount Validation**: Ensured that the `Billing Amount` column contained numeric values, and handled any discrepancies.

3. **Data Warehousing (AWS Redshift)**
   - **Star Schema Design**: A star schema was designed in AWS Redshift for efficient querying:
     - **Fact Table**: `patient_admissions` (contains details of patient admissions, billing amounts, dates, etc.)
     - **Dimension Tables**: `patients`, `doctors`, `hospitals`, and `insurance_providers` (related data for analysis).
   - **Data Loading**: Cleaned and transformed data was loaded into AWS Redshift using **SQL** and **Python (Boto3)** to automate the ETL pipeline.

4. **Data Analysis (SQL in Redshift)**
   - Performed advanced data analysis using **SQL** queries in AWS Redshift:
     - **Average Billing Analysis**: Calculated the average billing amount per hospital and medical condition.
     - **Readmission Rate Analysis**: Tracked readmission rates across hospitals.
     - **Condition Trends**: Analyzed common medical conditions based on age, gender, and hospital.
   - The queries were designed to provide actionable insights into hospital performance, patient demographics, and treatment trends.

5. **Data Visualization**
   - Used **AWS Redshift’s built-in charting capabilities** to visualize the results of the SQL queries.
   - Created key visualizations such as:
     - Average billing amount by hospital and condition.
     - Readmission rates by hospital.
     - Most common medical conditions across different age groups.
   - The charts were used to gain insights into healthcare trends and help healthcare providers make data-driven decisions.

## Technologies Used:
- **AWS S3** for data storage and ingestion.
- **AWS Lambda** for data cleaning, transformation, and automation of the ETL pipeline.
- **AWS Redshift** for data warehousing, querying, and analysis.
- **SQL** for querying and aggregating data in Redshift.
- **Python (Boto3)** for interacting with AWS services.
- **AWS QuickSight** (optional for future visualization, but used Redshift's built-in charting for this project).

## Key Learnings:
- Understanding of **ETL pipelines** and the use of AWS services for data processing.
- Data cleaning, transformation, and validation techniques.
- Designing and optimizing data warehouses in **AWS Redshift**.
- Running SQL queries to derive meaningful insights from structured data.
- Using **AWS Lambda** for automating ETL processes in real-time.

## Conclusion:
This project demonstrates the use of AWS services to create an efficient and scalable data engineering pipeline for healthcare data. It covers the entire ETL process, from data ingestion to cleaning, transformation, and analysis. The insights gained from this pipeline can be used for decision-making and optimizing healthcare operations.
