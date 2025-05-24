import mysql.connector
from clickhouse_driver import Client
import time
import datetime

mysql_conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="sales_db"
)
mysql_cursor = mysql_conn.cursor(dictionary=True)

ch_client = Client(host='clickhouse')

ch_client.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        transaction_time DateTime,
        product_id UInt32,
        quantity UInt32,
        unit_price Float32
    ) ENGINE = MergeTree()
    ORDER BY transaction_time
""")

mysql_cursor.execute("SELECT MIN(transaction_time) as min_time FROM sales")
result = mysql_cursor.fetchone()
last_time = result['min_time']

print(last_time, "lasttime")

while True:
    query = """
        SELECT transaction_time, product_id, quantity, unit_price
        FROM sales
        WHERE transaction_time > %s
        ORDER BY transaction_time
    """
    mysql_cursor.execute(query, (last_time,))
    rows = mysql_cursor.fetchall()

    if rows:
        values = [
            (row["transaction_time"], row["product_id"], row["quantity"], row["unit_price"])
            for row in rows
        ]
        ch_client.execute("""
            INSERT INTO sales (transaction_time, product_id, quantity, unit_price)
            VALUES
        """, values)
        last_timestamp = max(row["transaction_time"] for row in rows)
    else:
        print("no data")

    time.sleep(20)
