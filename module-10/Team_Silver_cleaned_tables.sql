
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    position VARCHAR(50)
);

CREATE TABLE Products_Suppliers (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    supplier_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    date_added DATE,
    supplier_name VARCHAR(100) NOT NULL
);

CREATE TABLE Transactions (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products_Suppliers(product_id)
);

CREATE TABLE Trips_Bookings (
    trip_id INT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    departure_date DATE NOT NULL,
    return_date DATE NOT NULL,
    customer_id INT NOT NULL,
    booking_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Users(user_id)
);
