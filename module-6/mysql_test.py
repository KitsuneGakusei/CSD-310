# test_mysql.py
import mysql.connector
from mysql.connector import errorcode

# Use dotenv_values to load .env
from dotenv import dotenv_values
secrets = dotenv_values(".env")  # Load from .env file in the same folder

# Create config dictionary
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True  # Optional but useful for debugging
}

# Test connection
try:
    db = mysql.connector.connect(**config)
    print("\n✅ Database user '{}' connected to MySQL on host '{}' with database '{}'".format(
        config["user"], config["host"], config["database"]
    ))
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("❌ Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("❌ Database does not exist.")
    else:
        print("❌", err)
