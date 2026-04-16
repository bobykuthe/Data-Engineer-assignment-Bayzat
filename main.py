import boto3
from config import SQS_ENDPOINT, QUEUE_NAME
from transformer import transform
from db import insert_data, create_table

sqs = boto3.client(
    "sqs",
    endpoint_url=SQS_ENDPOINT,
    region_name="ap-south-1"
)

def get_queue_url():
    response = sqs.get_queue_url(QueueName=QUEUE_NAME)
    return response["QueueUrl"]

def process_messages():
    queue_url = get_queue_url()

    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10
        )

        messages = response.get("Messages", [])

        if not messages:
            print("No more messages")
            break

        for msg in messages:
            body = msg["Body"]

            data = transform(body)

            if data:
                insert_data(data)
                print("Inserted:", data)
            else:
                print("Skipped malformed message")

            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg["ReceiptHandle"]
            )

if __name__ == "__main__":
    create_table()
    process_messages()
