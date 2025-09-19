# Serverless ETL Pipeline for Crypto Price Monitoring 🪙

##  Overview
This project extracts real-time crypto prices using a public API (CoinGecko), processes the data using AWS Lambda, stores it in S3 (raw & transformed), and optionally visualizes it using Jupyter Notebook locally.

## ☁️ Tech Stack
- **AWS Lambda**
- **AWS S3**
- **Amazon EventBridge** (for scheduling)
- **AWS DynamoDB** (optional logging)
- **Jupyter Notebook** (for local analysis)
- **Python, Boto3, Pandas, Matplotlib**

## 📊 Architecture
<p align="center">
  <img src="diagram.png" alt="architecture" width="600"><br><br>

## 📁 Project Structure
```
serverless-etl-crypto/
│
├── 📄 extract_to_s3.py          # Lambda function for data extraction
├── 📊 crypto_data_analysis.ipynb # Jupyter notebook for analysis
├── 🖼️  diagram.png              # Architecture diagram
├── 📖 README.md                 # Project documentation
```

## 🚀 How It Works
1. Lambda extracts crypto price from API.
2. Stores raw + transformed JSON in S3.
3. EventBridge triggers Lambda periodically.
4. Notebook fetches latest S3 data using Boto3 and visualizes it.





