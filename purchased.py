import mysql.connector
from dbconnection import get_database_connection
from prettytable import PrettyTable

def create_item_purchased(transaction_id):
    try:
        # Get a database connection
        connection = get_database_connection()

        while True:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            print()
            print("Create Item Purchased:")

            # Get input for item purchased details
            purchased_id = input("Enter Purchased ID: ")
            pur_product_id = input("Enter Product ID: ")
            purchased_quantity = input("Enter Purchased Quantity: ")
            purchased_price = input("Enter Purchased Price: ")
            timestamp = input("Enter Timestamp (Hour:Minute:Second): ")
            subtotal = input("Enter Subtotal: ")
            
            # Check if ProductID exists
            query_prod = "SELECT ProductID FROM product WHERE ProductID = %s"
            cursor.execute(query_prod, (pur_product_id,))
            product_result = cursor.fetchone()

            # Execute a query to insert the new item purchased into the database
            if product_result:
                query = "INSERT INTO itempurchased (PurchasedID, TransactionID, ProductID, PurchasedQuantity, PurchasedPrice, Timestamp, Subtotal) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (purchased_id, transaction_id, pur_product_id, purchased_quantity, purchased_price, timestamp, subtotal))

                # Commit the changes
                connection.commit()

                print("Item Purchased record created successfully!")

            else:
                print("ProductID does not exist. Item Purchased creation canceled.")

            cursor.close()

            more_purchased = input("Do you have more products to input? (yes/no): ").lower()
            if more_purchased != 'yes':
                break

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            connection.close()
            
def update_itempurchased():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Item Purchased:")

        # Get input for item purchased update
        purchased_id = input("Enter Purchased ID to update: ")

        # Check if PurchasedID exists
        query_itempurchased = "SELECT * FROM itempurchased WHERE PurchasedID = %s"
        cursor.execute(query_itempurchased, (purchased_id,))
        itempurchased_result = cursor.fetchone()

        if itempurchased_result:
            print()
            print("Current Item Purchased Data:")
            print("Purchased ID:", itempurchased_result[0])
            print("Transaction ID:", itempurchased_result[1])
            print("Product ID:", itempurchased_result[2])
            print("Purchased Quantity:", itempurchased_result[3])
            print("Purchased Price:", itempurchased_result[4])
            print("Timestamp :", itempurchased_result[5])
            print("Subtotal:", itempurchased_result[6])
            # Add other columns as needed

            print()
            # Get input for updating item purchased details
            new_transaction_id = input("Enter new Transaction ID (- to skip): ")
            new_product_id = input("Enter new Product ID (- to skip): ")
            new_purchased_quantity = input("Enter new Purchased Quantity (- to skip): ")
            new_purchased_price = input("Enter new Purchased Price (- to skip): ")
            new_timestamp = input("Enter new Timestamp (Hour:Minute:Second) (- to skip): ")
            new_subtotal = input("Enter new Subtotal (- to skip): ")
            # Add other variables for additional columns as needed

            # Check if the new TransactionID exists
            if new_transaction_id != '-' and not transaction_exists(cursor, new_transaction_id):
                print("Transaction ID does not exist. Update canceled.")
                return

            # Check if the new ProductID exists
            if new_product_id != '-' and not product_exists(cursor, new_product_id):
                print("Product ID does not exist. Update canceled.")
                return

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE itempurchased SET "
            update_data = []

            if new_transaction_id != '-':
                update_query += "TransactionID = %s, "
                update_data.append(new_transaction_id)

            if new_product_id != '-':
                update_query += "ProductID = %s, "
                update_data.append(new_product_id)

            if new_purchased_quantity != '-':
                update_query += "PurchasedQuantity = %s, "
                update_data.append(new_purchased_quantity)

            if new_purchased_price != '-':
                update_query += "PurchasedPrice = %s, "
                update_data.append(new_purchased_price)

            if new_timestamp != '-':
                update_query += "Timestamp = %s, "
                update_data.append(new_timestamp)

            if new_subtotal != '-':
                update_query += "Subtotal = %s, "
                update_data.append(new_subtotal)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the item purchased to update
            update_query += " WHERE PurchasedID = %s"
            update_data.append(str(purchased_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Item purchased data updated successfully!")

        else:
            print("PurchasedID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def transaction_exists(cursor, transaction_id):
    # Check if the TransactionID exists in the salestransaction table
    query_transaction = "SELECT TransactionID FROM salestransaction WHERE TransactionID = %s"
    cursor.execute(query_transaction, (transaction_id,))
    return cursor.fetchone() is not None

def product_exists(cursor, product_id):
    # Check if the ProductID exists in the product table
    query_product = "SELECT ProductID FROM product WHERE ProductID = %s"
    cursor.execute(query_product, (product_id,))
    return cursor.fetchone() is not None

def view_item_purchased_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to fetch all records from the itempurchased table
        query = "SELECT * FROM itempurchased"
        cursor.execute(query)

        # Fetch all the records
        itempurchased_records = cursor.fetchall()

        # Check if there are any records
        if not itempurchased_records:
            print("No records found in the itempurchased table.")
            return

        # Get the column names
        columns = [desc[0] for desc in cursor.description]

        # Create a PrettyTable object
        table = PrettyTable(columns)

        # Add rows to the PrettyTable
        for record in itempurchased_records:
            # Convert each column value to a string
            formatted_record = [str(value) if value is not None else "" for value in record]

            table.add_row(formatted_record)

        # Print the PrettyTable
        print(table)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
