# movies_queries.py

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Load secrets from the .env file
secrets = dotenv_values(".env")

# Configuration for MySQL connection
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

# Connect to the database
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n✅ Successfully connected to the '{}' database as user '{}'.".format(
        config["database"], config["user"]
    ))

    # 1. SELECT all fields from studio table
    print("\n-- DISPLAYING Studio RECORDS --")
    query1 = "SELECT * FROM studio;"
    cursor.execute(query1)
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}, Studio Name: {studio[1]}")

    # 2. SELECT all fields from genre table
    print("\n-- DISPLAYING Genre RECORDS --")
    query2 = "SELECT * FROM genre;"
    cursor.execute(query2)
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}, Genre Name: {genre[1]}")

    # 3. SELECT movie names for movies with run time < 120 mins
    print("\n-- DISPLAYING Short Film RECORDS --")
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
    cursor.execute(query3)
    short_films = cursor.fetchall()
    for film in short_films:
        print(f"Film Name: {film[0]}, Runtime: {film[1]} minutes")

    # 4. SELECT film names and directors, grouped by director
    print("\n-- DISPLAYING Director RECORDS in Group --")
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
    cursor.execute(query4)
    films_by_director = cursor.fetchall()
    for film in films_by_director:
        print(f"Director: {film[1]} - Film Name: {film[0]}")

    # Close the cursor and connection
    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("❌ Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("❌ Database does not exist.")
    else:
        print("❌", err)
