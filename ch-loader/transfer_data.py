import os
import mysql.connector
from clickhouse_connect import Client
import pandas as pd

def main():
    # Подключение к MySQL
    mysql_conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "mydb")
    )
    mysql_cursor = mysql_conn.cursor()

    mysql_cursor.execute("SELECT id, name, email FROM customers")
    rows = mysql_cursor.fetchall()

    df = pd.DataFrame(rows, columns=["id", "name", "email"])

    # Подключение к ClickHouse
    ch_client = Client(
        host=os.getenv("CLICKHOUSE_HOST", "localhost"),
        port=9000,
        username="default",
        password=""
    )

    # Создаем таблицу в ClickHouse (если нет)
    ch_client.command("""
    CREATE TABLE IF NOT EXISTS customers (
        id UInt32,
        name String,
        email String
    ) ENGINE = MergeTree()
    ORDER BY id
    """)

    # Записываем данные в ClickHouse
    ch_client.insert_dataframe("customers", df)

    print("Data transferred from MySQL to ClickHouse")

    mysql_cursor.close()
    mysql_conn.close()

if __name__ == "__main__":
    main()
