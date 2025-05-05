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

#write the Python script to create the tables in MySQL, and populate each with at least 6 records
cursor.execute("CREATE TABLE customer (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
db.commit()
cursor.execute("CREATE TABLE employee (employee_id INT AUTO_INCREMENT PRIMARY KEY, employee_name VARCHAR(55))")
db.commit()
cursor.execute("CREATE TABLE trip (trip_id INT AUTO_INCREMENT PRIMARY KEY, trip_name VARCHAR(255), trip_price INT, customer_id INT, employee_id INT)")
db.commit()

cursor.execute("ALTER TABLE trip ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id)")
db.commit()
cursor.execute("ALTER TABLE trip ADD FOREIGN KEY (employee_id) REFERENCES employee(employee_id)")
db.commit()

#Then we'd use this to display our data

#Write a python script that displays the data in each table, and take a screenshot of the results of the script that displays the data in each table.

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)


#or we can use a def method, but that's extra work.

#the end


#db.close()


