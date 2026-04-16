#!/bin/bash

echo "Starting services..."
docker-compose up -d

echo "Waiting for services..."
sleep 10

echo "Running ETL..."
python src/main.py
