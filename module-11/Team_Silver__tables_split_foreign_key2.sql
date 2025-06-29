
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(100) NOT NULL,
    customer_phone VARCHAR(20), 
    ecommerce_prospect VARCHAR(3) NOT NULL
);
CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
	employee_email VARCHAR(100) NOT NULL,
    employee_phone VARCHAR(20),
    employee_position VARCHAR(100) NOT NULL
    );
CREATE TABLE equipment (
    equipment_id INT PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
    purchase_price DECIMAL(10, 2) NOT NULL,
    rent_price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    date_purchased DATE NOT NULL 
);
 
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    equipment_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    equipment_purchased VARCHAR(3) NOT NULL,
    transaction_price DECIMAL(10, 2) NOT NULL,
    # aggregate customer transaction_price ammounts for transaction total in trips
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);
 
CREATE TABLE trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    guide INT NOT NULL,
	customer_id INT NOT NULL,
    departure_date DATE NOT NULL,
    return_date DATE NOT NULL,
    trip_price DECIMAL(10, 2) NOT NULL,
    transaction_total DECIMAL(10, 2),
    #aggregate trip_price & transaction_total using SUM for total_price
    total_price DECIMAL(10, 2),
	FOREIGN KEY (guide) REFERENCES employees(employee_id), 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
	); 



