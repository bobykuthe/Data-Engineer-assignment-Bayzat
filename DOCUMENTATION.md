# SQS ETL Project

## Setup
```bash
pip install -r requirements.txt
docker-compose up
```

## Run
```bash
./message-generator
python src/main.py
```

## Description
This project reads messages from AWS SQS (Localstack), transforms them, and stores them in PostgreSQL.

## Challenges
- Handling multiple JSON formats
- Timestamp conversion
- Localstack integration
