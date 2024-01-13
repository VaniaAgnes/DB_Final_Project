import mysql.connector
from dbconnection import get_database_connection
from prettytable import PrettyTable
from datetime import datetime

# no 9 is still iffy, fix it

def total_purchased_brand():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Most purchased quantity for each brand:")

        sql_query_one = """
                SELECT 
                    b.BrandName, 
                    SUM(ip.PurchasedQuantity) AS TotalPurchasedQuantity 
                FROM 
                    brand b 
                    INNER JOIN product p ON p.BrandID = b.BrandID
                    INNER JOIN itempurchased ip ON ip.ProductID = p.ProductID
                GROUP BY 
                    b.BrandName;
                """
        cursor.execute(sql_query_one)

        # Fetch and display the results
        for brand_name, total_purchased in cursor.fetchall():
            print(f"Brand: {brand_name}, Total Purchased Quantity: {total_purchased}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def product_low_quantity():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Products with low quantity (less than 25):")

        sql_query_one = """
                        SELECT 
                            p.ProductID,
                            p.ProductName,
                            i.StockQuantity
                        FROM 
                            product p
                            INNER JOIN inventory i ON p.ProductID = i.ProductID
                        WHERE 
                            i.StockQuantity < 25;
                        """
        cursor.execute(sql_query_one)

        # Fetch and display the results
        for product_id, product_name, stock_quantity in cursor.fetchall():
            print(f"Product ID: {product_id}, Product Name: {product_name}, Stock Quantity: {stock_quantity}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def retrieve_latest_restock():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nLatest Restock Dates for Each Product:")

        sql_query = """
                SELECT 
                    p.ProductID,
                    p.ProductName,
                    MAX(i.RestockDate) AS LatestRestockDate
                FROM 
                    inventory i
                    INNER JOIN product p ON i.ProductID = p.ProductID
                GROUP BY 
                    p.ProductID, p.ProductName;
                """
        cursor.execute(sql_query)

        # Fetch and display the results
        for product_id, product_name, latest_restock_date in cursor.fetchall():
            print(f"Product ID: {product_id}, Product Name: {product_name}, Latest Restock Date: {latest_restock_date}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def retrieve_transaction_on_specificDay(date_str):
    try:
        # Convert the date string to a date object
        transaction_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print(f"\nSales Transactions for {transaction_date}:")

        sql_query = """
                SELECT 
                    TransactionID, 
                    EmployeeID, 
                    TransactionDate, 
                    TotalAmount, 
                    PaymentStatus
                FROM 
                    salestransaction
                WHERE 
                    DATE(TransactionDate) = %s;
                """
        cursor.execute(sql_query, (transaction_date,))

        # Fetch and display the results
        for transaction_id, employee_id, transaction_date, total_amount, payment_status in cursor.fetchall():
            print(f"Transaction ID: {transaction_id}, Employee ID: {employee_id}, Date: {transaction_date}, Total Amount: {total_amount}, Payment Status: {payment_status}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def no_sale_products():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nProducts with No Sales:")

        sql_query = """
                SELECT 
                    p.ProductID, 
                    p.ProductName
                FROM 
                    product p
                    LEFT JOIN itempurchased ip ON p.ProductID = ip.ProductID
                WHERE 
                    ip.ProductID IS NULL;
                """
        cursor.execute(sql_query)

        # Fetch and display the results
        for product_id, product_name in cursor.fetchall():
            print(f"Product ID: {product_id}, Product Name: {product_name}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def get_total_revenue_cat():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nTotal Revenue for Each Category:")

        sql_query = """
                SELECT 
                    c.CategoryName,
                    SUM(ip.Subtotal) AS TotalRevenue
                FROM 
                    category c
                    INNER JOIN product p ON c.CategoryID = p.CategoryID
                    INNER JOIN itempurchased ip ON p.ProductID = ip.ProductID
                GROUP BY 
                    c.CategoryName;
                """
        cursor.execute(sql_query)

        # Fetch and display the results
        for category_name, total_revenue in cursor.fetchall():
            print(f"Category: {category_name}, Total Revenue: Rp.{total_revenue:.2f}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def average_transaction_amount():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nAverage Transaction Amount in Rupiah:")

        sql_query = """
                SELECT 
                    AVG(TotalAmount) AS AverageAmount
                FROM 
                    salestransaction;
                """
        cursor.execute(sql_query)

        # Fetch and display the result
        (average_amount,) = cursor.fetchone()
        print(f"Average Transaction Amount: Rp {average_amount:.2f}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def total_transactions_by_date():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nTotal Successful Sales Transactions by Date:")

        sql_query = """
                SELECT 
                    DATE(TransactionDate) AS TransactionDay,
                    COUNT(*) AS NumberOfTransactions
                FROM 
                    salestransaction
                WHERE 
                    PaymentStatus = 'Successful'  # Assuming 'Successful' indicates successful transactions
                GROUP BY 
                    DATE(TransactionDate);
                """
        cursor.execute(sql_query)

        # Fetch and display the results
        for transaction_day, number_of_transactions in cursor.fetchall():
            print(f"Date: {transaction_day}, Total Transactions: {number_of_transactions}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def check_mutations(start_date_str, end_date_str):
    try:
        # Convert the date strings to date objects
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print(f"\nDays with the Highest Number of Customers from {start_date} to {end_date}:")

        sql_query = """
                SELECT 
                    TransactionDate, 
                    TotalAmount
                FROM 
                    salestransaction
                WHERE 
                    TransactionDate BETWEEN %s AND %s
                ORDER BY 
                    TransactionDate;
                """
        cursor.execute(sql_query, (start_date, end_date))

        # Fetch and display the results
        for transaction_date, total_amount in cursor.fetchall():
            print(f"Date: {transaction_date}, Amount: {total_amount}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()

def brand_most_sales():
    try:
        # Establish a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print("\nBrand with the Most Sales:")

        sql_query = """
                SELECT 
                    b.BrandName,
                    SUM(ip.PurchasedQuantity) AS TotalSales
                FROM 
                    brand b
                    INNER JOIN product p ON b.BrandID = p.BrandID
                    INNER JOIN itempurchased ip ON p.ProductID = ip.ProductID
                GROUP BY 
                    b.BrandName
                ORDER BY 
                    TotalSales DESC
                LIMIT 1;
                """
        cursor.execute(sql_query)

        # Fetch and display the result
        result = cursor.fetchone()
        if result:
            brand_name, total_sales = result
            print(f"Brand: {brand_name}, Total Sales: {total_sales}")
        else:
            print("No sales data available.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()