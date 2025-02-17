# Healthcare Data Engineering Project

## Overview

This project focuses on building a data pipeline for a healthcare dataset using AWS services like Lambda, S3, Redshift, and Glue. The project involves data cleaning, transformation, and analysis to provide valuable insights from hospital admissions and patient data.

### Key Technologies Used:
- **AWS S3**: Storage for raw and processed data.
- **AWS Lambda**: Used for data cleaning and transformation.
- **AWS Redshift**: Data warehousing for structured query-based analysis.
- **SQL**: Used to perform data analysis on the Redshift warehouse.
- **AWS Glue**: Data cataloging and processing of data for Redshift.

---

## Project Steps

### 1. **Data Ingestion (AWS S3)**:
- The dataset was stored in an S3 bucket in CSV format.
- AWS Lambda was triggered when new files were uploaded to S3.

### 2. **Data Cleaning & Transformation (AWS Lambda)**:
- The Lambda function cleaned the dataset by:
  - Standardizing names, gender values, and medical conditions.
  - Converting date fields (Admission & Discharge dates) to correct formats.
  - Ensuring that Billing Amount is numeric.
  - Handling missing or incorrect values in test results and medication data.

### 3. **Data Warehousing (AWS Redshift)**:
- Designed and implemented a star schema in Redshift with a fact table `Patient_Admissions` and dimension tables like `Patients`, `Doctors`, `Hospitals`, and `Insurance_Providers`.
- Cleaned data was loaded into AWS Redshift using Python (Boto3).

### 4. **Data Analysis**:
- Performed SQL queries in Redshift to derive valuable insights like:
  - Average billing amount per hospital/condition.
  - Readmission rates per hospital.
  - Medical conditions by age & gender.

---

## How to Run the Project:

### Step 1: Setup AWS Services
- Set up **AWS S3** for storing data files.
- Set up **AWS Lambda** for data cleaning.
- Set up **AWS Redshift** for data warehousing.
- Load the dataset into S3 and trigger Lambda for processing.

### Step 2: Data Transformation
- Lambda functions are used to clean and transform data.

### Step 3: Load Cleaned Data into Redshift
- Load the cleaned data into Redshift using Python and Boto3.

### Step 4: Run SQL Queries
- Use SQL queries in Redshift to analyze the data and generate insights.

---

## Conclusion:

This project demonstrates the use of AWS services to process, clean, transform, and analyze healthcare data. The insights from this project can provide valuable metrics for hospitals, such as average billing amounts, readmission rates, and trends in medical conditions.

---
