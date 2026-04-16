SQS Data Pipeline ETL Tool
📌 Overview
This project implements a simple ETL (Extract, Transform, Load) pipeline that:
 Consumes messages from an AWS SQS queue (via Localstack)
 Transforms multiple event formats into a unified structure
 Stores the processed data into a PostgreSQL database
The solution is designed to be reproducible, scalable, and easy to run locally using Docker.
🏗️ Architecture
Localstack (SQS)
↓
Python ETL Tool
↓
Data Transformation
↓
PostgreSQL Database
⚙️ Tech Stack
 Language: Python 3
 Queue Service: AWS SQS (via Localstack)
 Database: PostgreSQL
 Containerization: Docker & Docker Compose
Why Python?
 Easy JSON processing
 Rich ecosystem (boto3 for AWS)
 Ideal for ETL pipelines and rapid development
📁 Project Structure
.
├── docker-compose.yml
├── requirements.txt
├── run.sh
├── DOCUMENTATION.md
└── src
├── main.py
├── transformer.py
├── db.py
└── config.py
🚀 Setup Instructions
1. Prerequisites
Make sure you have installed:
 Docker
 Docker Compose
 Python 3.x
 pip
2. Install Dependencies
pip install -r requirements.txt
3. Start Services
docker-compose up -d
This will start:
 Localstack (SQS service)
 PostgreSQL database
4. Generate Test Messages
Run the provided message generator:
./message-generators/linux # Linux
./message-generators/darwin # macOS
message-generators\\windows.exe # Windows
This will:
 Create an SQS queue (test-queue)
 Push sample messages into the queue
5. Run ETL Pipeline
python src/main.py
OR using script:
bash run.sh
🔄 ETL Process Explained
1. Extract
 Connects to SQS via Localstack
 Reads messages in batches
2. Transform
Handles multiple input formats:
Format 1: Route-based
"route": [
{"from": "A", "to": "B", "started_at": "..."}
]
Format 2: Location-based
"locations": [
{"location": "A", "timestamp": 123456}
]
Unified Output Format:
{
"id": 1,
"mail": "example@gmail.com",
"name": "Full Name",
"trip": {
"departure": "A",
"destination": "B",
"start_date": "timestamp",
"end_date": "timestamp"
}
}
3. Load
 Inserts transformed data into PostgreSQL
 Table: trips
🗄️ Database Schema
CREATE TABLE trips (
id INT,
mail TEXT,
name TEXT,
departure TEXT,
destination TEXT,
start_date TIMESTAMP,
end_date TIMESTAMP
);
⚠️ Error Handling
 Invalid JSON messages are skipped
 Malformed messages are logged
 Messages are deleted only after processing (ensures no duplication)
▶️ Usage Notes
 The tool runs until the queue is empty
 It can be executed multiple times safely
 Already processed messages are removed from the queue
️ Example Output
Inserted: {id: 3, ...}
Inserted: {id: 5, ...}
Skipped malformed message
No more messages
️ Challenges Faced
 Handling multiple input message formats
 Converting timestamps (string & epoch)
 Setting up Localstack correctly
 Ensuring idempotent message processing
 Managing malformed data safely
⭐ Bonus Features Implemented
 PostgreSQL added in Docker Compose
 Modular code structure
 Reusable ETL pipeline
 Error handling for bad messages
🔮 Future Improvements
 Add logging framework
 Add retry mechanism for failed inserts
 Use ORM (SQLAlchemy)
 Dockerize ETL service
 Add unit tests
🏁 Conclusion
This project demonstrates:
 Understanding of AWS SQS
 Data transformation skills
 ETL pipeline design
 Docker-based environment setup
It can be easily extended into a production-grade data pipeline
