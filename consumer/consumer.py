import logging
import os
import time

import pika
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)


def read_message():
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

    def message_callback(ch, method, properties, body):
        logging.info(f"I'm busy doing work for {body}")
        time.sleep(5)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task-queue", on_message_callback=message_callback)
    channel.start_consuming()
    conn.close()


if __name__ == "__main__":
    read_message()
