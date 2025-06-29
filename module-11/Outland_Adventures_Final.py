#Silver Group
#Rashai R.
#Crystal
#Tyspn B.

#CSD_310
#5/4/2025
#Module 10

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}
try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config)  # connect to the movies database

    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

#WE OFFICIALLY START HERE

#write the Python script to create the tables in MySQL
cursor.execute("CREATE TABLE customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(100) NOT NULL, customer_email VARCHAR(100) NOT NULL, customer_phone VARCHAR(20), ecommerce_prospect VARCHAR(3) NOT NULL)")
db.commit()
cursor.execute("CREATE TABLE employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(100) NOT NULL, employee_email VARCHAR(100) NOT NULL, employee_phone VARCHAR(20), employee_position VARCHAR(100) NOT NULL)")
db.commit()
cursor.execute("CREATE TABLE equipment (equipment_id INT PRIMARY KEY, equipment_name VARCHAR(100) NOT NULL, purchase_price DECIMAL(10, 2) NOT NULL, rent_price DECIMAL(10, 2) NOT NULL, stock INT NOT NULL, date_purchased DATE NOT NULL)")
db.commit()
cursor.execute("CREATE TABLE transactions (transaction_id INT PRIMARY KEY, customer_id INT NOT NULL, equipment_id INT NOT NULL, transaction_date DATE NOT NULL, equipment_purchased VARCHAR(3), transaction_price DECIMAL(10, 2) NOT NULL)")
db.commit()
cursor.execute("CREATE TABLE trips (trip_id INT PRIMARY KEY, location VARCHAR(100), guide INT NOT NULL, customer_id INT NOT NULL, departure_date DATE NOT NULL, return_date DATE NOT NULL, trip_price DECIMAL(10, 2) NOT NULL, transaction_total DECIMAL(10, 2), total_price DECIMAL(10, 2))")
db.commit()


#adding foreign keys

cursor.execute("ALTER TABLE transactions ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id)")
db.commit()
cursor.execute("ALTER TABLE transactions ADD FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)")
db.commit()
cursor.execute("ALTER TABLE trips ADD FOREIGN KEY (guide) REFERENCES employees(employee_id)")
db.commit()
cursor.execute("ALTER TABLE trips ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id)")
db.commit()

#populate each with at least 6 records
insert1 = "INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone, ecommerce_prospect) VALUES (%s, %s, %s, %s, %s)"
values1 = [
    (1, 'John Hancock', 'JHancock@gmail.com', '202-918-2132', 'yes'),
    (2, 'Norris Mixon', 'MixonNorris@gmail.com', '505-644-6684', 'no'),
    (3, 'Sylas Watts', 'WattsS3@gmail.com', '472-271-6978', 'no'),
    (4, 'Yekara Mcdowell', 'YMcdowell@gmail.com', '316-502-4351', 'no'),
    (5, 'Aaliyah Nicholson', 'NicholsonA@gmail.com', '215-884-5238', 'yes'),
    (6, 'Mabel Simmons', 'Ma2ThaDEA@gmail.com', '610-981-1632', 'yes')
]
# executemany() method
cursor.executemany(insert1, values1)
db.commit()

#employees
insert2 = "INSERT INTO employees (employee_id, employee_name, employee_email, employee_phone, employee_position) VALUES (%s, %s, %s, %s, %s)"
values2 = [
    (1, 'Blythe Timmerson', 'BlytheT@outland.com', '484-918-2132', 'owner'),
    (2, 'Jim Ford', 'JimF@outland.com', '484-644-6684','owner'),
    (3, 'John MacNell', 'Mac@outland.com', '484-271-6978', 'guide'),
    (4, 'Duke Marland', 'Duke@outland.com', '484-502-4351', 'guide'),
    (5, 'Anita Gallegos', 'GallegosA@outland.com', '484-884-5238', 'advertising manager'),
    (6, 'Dimitrios Stravopolous', 'DimitriosS@outland.com', '484-981-1632', 'equipment manager'),
    (7, 'Mei Wong', 'MWong@outland.com', '484-981-1632', 'developer'),
]
# executemany() method
cursor.executemany(insert2, values2)
db.commit()

#equipment
insert3 = "INSERT INTO equipment (equipment_id, equipment_name, purchase_price, rent_price, stock, date_purchased) VALUES (%s, %s, %s, %s, %s, %s)"
values3 = [
    (11, 'Tent', 700.99, 99.99, 15, '2021-12-13'),
    (12, 'Stove', 75.00, 15.00, 10, '2025-05-03'),
    (13, 'Camping kit', 32.99, 10.00, 20, '2023-09-08'),
    (14, 'Trekking pole', 100.00, 20.00, 6, '2019-01-15'),
    (15, 'Emergency kit', 30.00, 5.00, 10, '2025-05-03'),
    (16, 'Cooler', 120.00, 40.00, 3, '2022-06-05')
]
# executemany() method
cursor.executemany(insert3, values3)
db.commit()


#transactions
insert4 = "INSERT INTO transactions (transaction_id, customer_id, equipment_id, transaction_date, equipment_purchased, transaction_price) VALUES (%s, %s, %s, %s, %s, %s)"
values4 = [
    (100, 2, 11,'2025-02-10', 'No' , 99.99),
    (101, 2, 13, '2025-02-10', 'Yes', 32.99),
    (102, 4, 11, '2025-04-15', 'Yes', 700.99),
    (103, 5, 15, '2025-01-20', 'Yes' , 30.00),
    (104, 5, 16, '2025-01-20', 'Yes', 120.00),
    (105, 6, 14, '2025-03-17', 'No', 20.00),
    (106, 6, 15, '2025-03-17', 'Yes', 30.00),
    (107, 6, 16, '2025-03-17', 'Yes', 120.00),
    (108, 1, 12, '2025-02-11', 'No', 15.00),
    (110, 1, 16, '2025-02-11', 'Yes', 120.00),
    (111, 3, 13, '2025-05-11', 'Yes', 32.99),
]
# executemany() method
cursor.executemany(insert4, values4)
db.commit()

#trips
insert5 = "INSERT INTO trips (trip_id, location, guide, customer_id, departure_date, return_date, trip_price, transaction_total, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
values5 = [
    (200, 'Asia', 3, 2, '2025-06-05', '2025-06-10', 2500.00, None, None),
    (201, 'Africa', 4, 4, '2025-06-05', '2025-06-10', 2200.99, None, None),
    (202, 'Africa', 4, 5, '2025-05-05', '2025-05-15', 3600.00, None, None),
    (203, 'South Europe', 3, 6, '2025-07-05', '2025-07-12', 2700.00, None, None),
    (204, 'Africa', 3, 1, '2025-08-05', '2025-08-10', 2500.00, None, None),
    (205, 'Asia', 4, 3, '2025-07-05', '2025-07-20', 4500.00, None, None),
]
# executemany() method
cursor.executemany(insert5, values5)
db.commit()
#Then we'd use this to display our data

#Write a python script that displays the data in each table, and take a screenshot of the results of the script that displays the data in each table.
print ("--showing tables--")
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)
print()
#showing data in tables
#we can use a def method later, but that's extra work right now.
print ("--showing records from customers--")
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
print ("--showing records from employees--")
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
print ("--showing records from equipment--")
cursor.execute("SELECT * FROM equipment")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
print ("--showing records from transactions--")
cursor.execute("SELECT * FROM transactions")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()
print ("--showing records from trips--")
cursor.execute("SELECT * FROM trips")
rows = cursor.fetchall()
for row in rows:
    print(row)

#the end
db.close()


