import mysql.connector
import random
from datetime import datetime, timedelta
import time

time.sleep(15)

mysql_conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="sales_db"
)

mysql_cursor = mysql_conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT,
    price INT,
    sale_date DATE
)
'''
mysql_cursor.execute(create_table)
print("Таблица есть")
products = [
    ('Товар 1', 10),
    ('Товар 2', 15),
    ('Товар 3', 7),
    ('Товар 4', 14),
    ('Товар 5', 2),
    ('Товар 6', 4),
    ('Товар 7', 5),
    ('Товар 8', 10),
    ('Товар 9', 8),
    ('Товар 10', 16)
]

def random_date_2024():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).date()


records = []
for _ in range(10000):
    product = random.choice(products)
    product_name = product[0]
    price = product[1]
    quantity = random.randint(1, 10)
    sale_date = random_date_2024()
    records.append((product_name, quantity, price, sale_date))


insert_query = '''
INSERT INTO sales (product_name, quantity, price, sale_date)
VALUES (%s, %s, %s, %s)
'''

mysql_cursor.executemany(insert_query, records)
mysql_conn.commit()

print(f"Inserted {mysql_cursor.rowcount} rows.")

mysql_cursor.close()
mysql_conn.close()
