import boto3
import csv
import io
import json
import uuid  # For generating unique IDs

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileMetadata')  # Replace with your table name

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            # Fetch the .csv file from S3
            response = s3_client.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')

            # Parse the .csv file
            csv_reader = csv.DictReader(io.StringIO(content))

            # Insert each row into DynamoDB
            for row in csv_reader:
                # Use a unique identifier for each row
                table.put_item(Item={
                    "UniqueID": str(uuid.uuid4()),  # Unique key for each row
                    "FileName": key,  # File the row belongs to
                    "Name": row['Name'],
                    "Age": row['Age'],
                    "Email": row['Email']
                })

        return {
            "statusCode": 200,
            "body": json.dumps("CSV data processed and stored in DynamoDB.")
        }
    except Exception as e:
        print(f"Error processing file: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing file.")
        }
