import random
import datetime
import time
import mysql.connector

time.sleep(10)

conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="sales_db"
)
cursor = conn.cursor()

products = list(range(1, 21))

for _ in range(1000):
    transaction_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
    product_id = random.choice(products)
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(10, 100), 2)
    cursor.execute("""
        INSERT INTO sales (transaction_time, product_id, quantity, unit_price)
        VALUES (%s, %s, %s, %s)
    """, (transaction_time, product_id, quantity, unit_price))

conn.commit()
print("Готово!")
