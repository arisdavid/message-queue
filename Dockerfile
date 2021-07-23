FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

ADD consumer/requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .