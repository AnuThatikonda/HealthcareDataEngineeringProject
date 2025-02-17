import pandas as pd
import boto3
from io import StringIO

# Initialize S3 client
s3 = boto3.client("s3")

def lambda_handler(event, context):
    # S3 bucket and file details from the event
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_key = event["Records"][0]["s3"]["object"]["key"]

    # Read CSV file from S3
    obj = s3.get_object(Bucket=s3_bucket, Key=s3_file_key)
    df = pd.read_csv(obj["Body"])

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Standardize name capitalization
    df["name"] = df["name"].str.title()

    # Standardize gender values
    df["gender"] = df["gender"].str.capitalize()

    # Convert date fields to datetime format
    df["date_of_admission"] = pd.to_datetime(df["date_of_admission"])
    df["discharge_date"] = pd.to_datetime(df["discharge_date"])

    # Convert billing amount to numeric
    df["billing_amount"] = pd.to_numeric(df["billing_amount"], errors="coerce")

    # Handle missing data
    df["test_results"] = df["test_results"].fillna("Unknown")
    df["medication"] = df["medication"].fillna("None")

    # Save cleaned data back to S3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=s3_bucket, Key="cleaned/" + s3_file_key, Body=csv_buffer.getvalue())

    return {
        'statusCode': 200,
        'body': 'Data cleaning complete and uploaded to S3.'
    }
