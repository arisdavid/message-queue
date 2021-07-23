FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

ADD producer /producer
RUN pip3 install -r producer/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/producer"

CMD ["python3", "-u", "/producer/producer.py"]