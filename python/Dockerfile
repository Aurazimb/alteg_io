FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY generate_data_mysql.py .
COPY transfer_to_clickhouse.py .
