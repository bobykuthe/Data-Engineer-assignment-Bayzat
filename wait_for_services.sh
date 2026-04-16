#!/bin/bash

echo "Waiting for Localstack..."
sleep 10

echo "Waiting for PostgreSQL..."
sleep 5

echo "Starting ETL..."
python src/main.py
