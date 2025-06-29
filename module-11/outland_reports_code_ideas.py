import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values
from datetime import datetime

# Load environment variables from .env
secrets = dotenv_values(".env")

# Configure database connection
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print(f"\nReport generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Report 1: Equipment Sales Summary
    cursor.execute("""
        SELECT 
            ps.product_id,
            ps.product_name,
            SUM(t.quantity) AS total_units_sold,
            SUM(t.total_amount) AS total_revenue
        FROM Transactions t
        JOIN Products_Suppliers ps ON t.product_id = ps.product_id
        GROUP BY ps.product_id, ps.product_name
        ORDER BY total_revenue DESC;
    """)
    print("\nReport 1: Equipment Sales Summary")
    print("Product ID | Product Name | Units Sold | Total Revenue")
    for row in cursor.fetchall():
        print(row)

    # Report 2: Regional Booking Trends
    cursor.execute("""
        SELECT 
            location,
            YEAR(booking_date) AS year,
            COUNT(*) AS total_bookings
        FROM Trips_Bookings
        GROUP BY location, YEAR(booking_date)
        ORDER BY location, year;
    """)
    print("\nReport 2: Regional Booking Trends")
    print("Location | Year | Total Bookings")
    for row in cursor.fetchall():
        print(row)

    # Report 3: Aging Inventory Report
    cursor.execute("""
        SELECT 
            product_id,
            product_name,
            date_added,
            DATEDIFF(CURDATE(), date_added) / 365 AS age_in_years
        FROM Products_Suppliers
        WHERE date_added < CURDATE() - INTERVAL 5 YEAR;
    """)
    print("\nReport 3: Aging Inventory Report")
    print("Product ID | Product Name | Date Added | Age in Years")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Check your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)