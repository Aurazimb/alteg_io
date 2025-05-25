CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);
