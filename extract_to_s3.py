import json
import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'serverless-etl-pipeline-akanksha'  # Your bucket name

def lambda_handler(event, context):
    # Step 1: Extract live crypto data
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd'
    response = requests.get(url)

    if response.status_code != 200:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': '❌ Failed to fetch crypto data'})
        }

    data = response.json()

    # Step 2: Save raw data to S3
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')
    raw_key = f'raw-data/crypto-live-{timestamp}.json'
    
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=raw_key,
        Body=json.dumps(data)
    )
    print(f"✅ Raw crypto data saved to S3: {raw_key}")

    # Step 3: Transform into flat format
    transformed_data = []
    processed_at = datetime.utcnow().isoformat()

    for coin, values in data.items():
        transformed_data.append({
            'base_asset': coin,
            'price': values['usd'],
            'timestamp': processed_at
        })

    # Step 4: Save transformed data to S3 in record (array) format
    processed_key = f'processed-data/crypto-transformed-{timestamp}.json'
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=processed_key,
        Body=json.dumps(transformed_data)
    )
    print(f"✅ Transformed crypto data saved to S3: {processed_key}")

    # Step 5: Final response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': '✅ Crypto data processed and saved successfully',
            'raw_file': f's3://{BUCKET_NAME}/{raw_key}',
            'processed_file': f's3://{BUCKET_NAME}/{processed_key}',
            'timestamp': timestamp
        })
    }
