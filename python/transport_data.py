import mysql.connector
import clickhouse_connect
import sys
import time

BATCH_SIZE = 5000

time.sleep(20)

mysql_conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="sales_db"

)

mysql_conn.autocommit = True  
mysql_cursor = mysql_conn.cursor(dictionary=True)
print("mysql connect")


ch_client = clickhouse_connect.get_client(
    host='clickhouse',
    port=8123,
    username='username',
    password='changeme',
    database='my_database',
)
print("click connect ")

create_table = '''
CREATE TABLE IF NOT EXISTS sales (
    id UInt32,
    product_name String,
    quantity UInt32,
    price Float32,
    sale_date Date
) ENGINE = MergeTree()
ORDER BY id
'''


ch_client.command(create_table)
print('Создали таблицу')

def query_from_mysql(id):
    mysql_cursor.execute(
        f'''
        SELECT id, product_name, quantity, price, sale_date
        FROM sales
        WHERE id > {id}
        ORDER BY id
        LIMIT {BATCH_SIZE}
        '''
    )
    return mysql_cursor.fetchall()

while True:
    last_id = '''
    select max(id)
    from my_database.sales s
    '''
    id = ch_client.query(last_id)
    id = id.result_rows[0][0]
    print(id, "ласт айди в таблице клика")

    mysql_cursor.execute(f'''
        SELECT id, product_name, quantity, price, sale_date
        FROM sales
        WHERE id > {id}
        ORDER BY id
        LIMIT {BATCH_SIZE}
    ''')
    rows = mysql_cursor.fetchall()
    print(len(rows), "Последний товар из запроса")
   


    if rows == []:
        print("Нет данныз")
        print("time")
        time.sleep(30)
    else:
        data = []
        for i in rows:
            data.append([i['id'], i['product_name'], i['quantity'], i['price'], i['sale_date']])
    
        ch_client.insert(
            'my_database.sales',
            data,
            column_names=['id', 'product_name', 'quantity', 'price', 'sale_date']
        )

        print(f"Данные загружены в Клик, {len(data)}")
        time.sleep(30)
