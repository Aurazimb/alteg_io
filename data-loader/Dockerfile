FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY fill_data.py .

CMD ["python", "fill_data.py"]
