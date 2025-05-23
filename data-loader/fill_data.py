import os
import mysql.connector

def main():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "mydb")
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
    """)

    cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Bob", "bob@example.com"))
    conn.commit()

    print("Data inserted into MySQL")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
