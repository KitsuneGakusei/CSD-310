# movies_update_and_delete.py

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

def show_films(cursor, title):
    print("\n -- {} --".format(title))
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    films = cursor.fetchall()
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n✅ Successfully connected to the '{}' database as user '{}'.".format(config["database"], config["user"]))

    # Display films before changes
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film
    insert_film = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Inception', 2010, 148, 'Christopher Nolan', 1, 2);
    """
    cursor.execute(insert_film)

    # Display films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien genre to Horror
    update_film = """
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien';
    """
    cursor.execute(update_film)

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete Gladiator
    delete_film = """
    DELETE FROM film
    WHERE film_name = 'Gladiator';
    """
    cursor.execute(delete_film)

    # Display films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    # Commit changes
    db.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("❌ Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("❌ Database does not exist.")
    else:
        print("❌", err)

finally:
    cursor.close()
    db.close()
