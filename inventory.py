import mysql.connector
from dbconnection import get_database_connection
from prettytable import PrettyTable

def create_inventory():
    try:
        # Get a database connection
        connection = get_database_connection()

        while True:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()
            print()
            print("Create Inventory Item:")
            
            # Get input for inventory item details
            inventory_id = input("Enter Inventory ID: ")
            inv_product_id = input("Enter Product ID: ")
            stock_quantity = input("Enter Stock Quantity: ")
            restock_date = input("Enter Restock Date (YYYY-MM-DD): ")
            shelf_location = input("Enter Shelf Location: ")

            # Check if ProductID exists
            query_prod = "SELECT ProductID FROM product WHERE ProductID = %s"
            cursor.execute(query_prod, (inv_product_id,))
            inventory_result = cursor.fetchone()

            # Execute a query to insert the new inventory item into the database
            if inventory_result:
                query = "INSERT INTO inventory (InventoryID, ProductID, StockQuantity, RestockDate, ShelfLocation) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (inventory_id, inv_product_id, stock_quantity, restock_date, shelf_location))

                # Commit the changes
                connection.commit()

                print("Inventory item created successfully!")

            else:
                print("ProductID does not exist. Inventory item creation canceled.")

            cursor.close()

            more_items = input("Do you have more items to input? (yes/no): ").lower()
            if more_items != 'yes':
                break

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            connection.close()

def delete_inventory():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Delete Inventory Item:")

        # Get input for inventory item deletion
        inventory_id = input("Enter Inventory ID to delete: ")

        # Check if InventoryID exists
        query_inventory = "SELECT InventoryID FROM inventory WHERE InventoryID = %s"
        cursor.execute(query_inventory, (inventory_id,))
        inventory_result = cursor.fetchone()

        # Execute a query to delete the inventory item from the database
        if inventory_result:
            # Delete the inventory item
            delete_query = "DELETE FROM inventory WHERE InventoryID = %s"
            cursor.execute(delete_query, (inventory_id,))

            # Commit the changes
            connection.commit()

            print("Inventory item deleted successfully!")

        else:
            print("InventoryID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            

def update_inventory():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Inventory Item:")

        # Get input for inventory item update
        inventory_id = input("Enter Inventory ID to update: ")

        # Check if InventoryID exists
        query_inventory = "SELECT * FROM inventory WHERE InventoryID = %s"
        cursor.execute(query_inventory, (inventory_id,))
        inventory_result = cursor.fetchone()

        if inventory_result:
            print()
            print("Current Inventory Item Data:")
            print("Inventory ID:", inventory_result[0])
            print("Product ID:", inventory_result[1])
            print("Stock Quantity:", inventory_result[2])
            print("Restock Date:", inventory_result[3])
            print("Shelf Location:", inventory_result[4])
            # Add other columns as needed

            print()
            # Get input for updating inventory item details
            new_product_id = input("Enter new Product ID (- to skip): ")
            new_stock_quantity = input("Enter new Stock Quantity (- to skip): ")
            new_restock_date = input("Enter new Restock Date (YYYY-MM-DD, - to skip): ")
            new_shelf_location = input("Enter new Shelf Location (- to skip): ")
            # Add other variables for additional columns as needed

            # Check if the new ProductID exists
            if new_product_id != '-' and not product_exists(cursor, new_product_id):
                print("Product ID does not exist. Update canceled.")
                return

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE inventory SET "
            update_data = []

            if new_product_id != '-':
                update_query += "ProductID = %s, "
                update_data.append(new_product_id)

            if new_stock_quantity != '-':
                update_query += "StockQuantity = %s, "
                update_data.append(new_stock_quantity)

            if new_restock_date != '-':
                update_query += "RestockDate = %s, "
                update_data.append(new_restock_date)

            if new_shelf_location != '-':
                update_query += "ShelfLocation = %s, "
                update_data.append(new_shelf_location)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the inventory item to update
            update_query += " WHERE InventoryID = %s"
            update_data.append(str(inventory_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Inventory item data updated successfully!")

        else:
            print("Inventory ID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def product_exists(cursor, product_id):
    # Check if the ProductID exists in the product table
    query_product = "SELECT ProductID FROM product WHERE ProductID = %s"
    cursor.execute(query_product, (product_id,))
    return cursor.fetchone() is not None


def view_inventory_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the inventory table
        query_inventory = "SELECT * FROM inventory"
        cursor.execute(query_inventory)

        # Fetch all rows
        inventory_data = cursor.fetchall()

        if not inventory_data:
            print("No data found in the inventory table.")
            return

        # Display header
        print("\nInventory Table:")
        print("| {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format("InventoryID", "ProductID", "StockQuantity", "RestockDate", "ShelfLocation"))
        print("-" * 85)

        # Display data
        for row in inventory_data:
            print("| {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format(row[0], row[1], row[2], row[3], row[4]))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def view_inventory_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to fetch all records from the inventory table
        query = "SELECT * FROM inventory"
        cursor.execute(query)

        # Fetch all the records
        inventory_records = cursor.fetchall()

        # Check if there are any records
        if not inventory_records:
            print("No records found in the inventory table.")
            return

        # Get the column names
        columns = [desc[0] for desc in cursor.description]

        # Create a PrettyTable object
        table = PrettyTable(columns)

        # Add rows to the PrettyTable
        for record in inventory_records:
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





