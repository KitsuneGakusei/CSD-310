import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values
from datetime import datetime
from tabulate import tabulate  # Add this import


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

    print(f"\nReport generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Report 1: Equipment Sales Summary
    cursor.execute("""
        SELECT 
            e.equipment_id,
            e.equipment_name,
            COUNT(t.transaction_id) AS total_transactions,
            SUM(t.transaction_price) AS total_revenue
        FROM transactions t
        JOIN equipment e ON t.equipment_id = e.equipment_id
        GROUP BY e.equipment_id, e.equipment_name
        ORDER BY total_revenue DESC;
    """)
    rows = cursor.fetchall()
    clean_rows = [(eid, name, trans, float(rev)) for eid, name, trans, rev in rows]
    print("Report 1: Equipment Sales Summary")
    print(tabulate(clean_rows, headers=["Equipment ID", "Equipment Name", "Total Transactions", "Total Revenue"], floatfmt=".2f"))
    print()

    # Report 2: Regional Booking Trends
    cursor.execute("""
        SELECT 
            location,
            YEAR(departure_date) AS year,
            COUNT(*) AS total_bookings
        FROM trips
        GROUP BY location, YEAR(departure_date)
        ORDER BY location, year;
    """)
    rows = cursor.fetchall()
    print("Report 2: Regional Booking Trends")
    print(tabulate(rows, headers=["Location", "Year", "Total Bookings"]))
    print()

    # Report 3: Aging Inventory Report
    cursor.execute("""
        SELECT 
            equipment_id,
            equipment_name,
            date_purchased,
            ROUND(DATEDIFF(CURDATE(), date_purchased) / 365, 1) AS age_in_years
        FROM equipment
        WHERE date_purchased < CURDATE() - INTERVAL 5 YEAR;
    """)
    rows = cursor.fetchall()
    print("Report 3: Aging Inventory Report")
    print(tabulate(rows, headers=["Equipment ID", "Equipment Name", "Date Purchased", "Age (Years)"]))
    print()

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Check your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
