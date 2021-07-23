import logging
import os
import time

import pika
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)


def send_message(message):
    credentials = pika.PlainCredentials(
        os.getenv("RMQ_USERNAME"), os.getenv("RMQ_PASSWORD")
    )
    conn = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RMQ_HOST"),
            port=os.getenv("RMQ_PORT"),
            credentials=credentials,
        )
    )
    channel = conn.channel()
    channel.queue_declare(queue="task-queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task-queue",
        body=message,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    logging.info(f"Published email: {message}")
    conn.close()


if __name__ == "__main__":
    fake = Faker()
    while True:
        fake_email = fake.email()
        send_message(fake_email)
        time.sleep(3)
