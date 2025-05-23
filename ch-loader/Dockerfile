FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY transfer_data.py .

CMD ["python", "transfer_data.py"]
