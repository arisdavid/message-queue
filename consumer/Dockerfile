FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

ADD consumer /consumer
RUN pip3 install -r consumer/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/consumer"

CMD ["python3", "-u", "/consumer/consumer.py"]