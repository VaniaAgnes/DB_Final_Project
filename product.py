import mysql.connector
from dbconnection import get_database_connection

def create_product():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Create Product:")

        # Get other product details from the user
        product_id = input("Enter Product ID for the new product: ")
        prod_brand_id = input("Enter Brand ID for the new product: ")
        prod_category_id = input("Enter Category ID for the new product: ")
        product_name = input("Enter Product Name: ")
        price = input("Enter Price: ")

        # Check if BrandID exists
        query_brand = "SELECT BrandID FROM brand WHERE BrandID = %s"
        cursor.execute(query_brand, (prod_brand_id,))
        brand_result = cursor.fetchone()

        # Check if CategoryID exists
        query_category = "SELECT CategoryID FROM category WHERE CategoryID = %s"
        cursor.execute(query_category, (prod_category_id,))
        category_result = cursor.fetchone()

        # If BrandID and CategoryID exist, proceed with the insertion
        if brand_result and category_result:
            query_insert = "INSERT INTO product (ProductID, BrandID, CategoryID, ProductName, Price) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query_insert, (product_id, prod_brand_id, prod_category_id, product_name, price))

            # Commit the changes
            connection.commit()

            cursor.close()
            connection.close()

            print("Product created successfully!")

        else:
            print("BrandID or CategoryID does not exist. Product creation canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def delete_product():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Delete Product:")

        # Get input for product deletion
        product_id = input("Enter Product ID to delete: ")

        # Check if ProductID exists
        query_product = "SELECT ProductID FROM product WHERE ProductID = %s"
        cursor.execute(query_product, (product_id,))
        product_result = cursor.fetchone()

        # Execute a query to delete the product from the database
        if product_result:
            delete_query = "DELETE FROM product WHERE ProductID = %s"
            cursor.execute(delete_query, (product_id,))

            # Commit the changes
            connection.commit()

            print("Product deleted successfully!")

        else:
            print("ProductID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            
import mysql.connector
from dbconnection import get_database_connection

def update_product():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Product:")

        # Get input for product update
        product_id = input("Enter Product ID to update: ")

        # Check if ProductID exists
        query_product = "SELECT * FROM product WHERE ProductID = %s"
        cursor.execute(query_product, (product_id,))
        product_result = cursor.fetchone()

        if product_result:
            print()
            print("Current Product Data:")
            print("ProductID:", product_result[0])
            print("Brand ID:", product_result[1])
            print("Category ID:", product_result[2])
            print("Product Name:", product_result[3])
            print("Price:", product_result[4])
            # Add other columns as needed

            print()
            # Get input for updating product details
            new_brand_id = input("Enter new Brand ID (- to skip): ")
            new_category_id = input("Enter new Category ID (- to skip): ")
            new_product_name = input("Enter new Product Name (- to skip): ")
            new_price = input("Enter new Price (- to skip): ")
            # Add other variables for additional columns as needed

            # Check if the new BrandID exists
            if new_brand_id != '-' and not brand_exists(cursor, new_brand_id):
                print("BrandID does not exist. Update canceled.")
                return

            # Check if the new CategoryID exists
            if new_category_id != '-' and not category_exists(cursor, new_category_id):
                print("CategoryID does not exist. Update canceled.")
                return

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE product SET "
            update_data = []

            if new_brand_id != '-':
                update_query += "BrandID = %s, "
                update_data.append(new_brand_id)

            if new_category_id != '-':
                update_query += "CategoryID = %s, "
                update_data.append(new_category_id)

            if new_product_name != '-':
                update_query += "ProductName = %s, "
                update_data.append(new_product_name)

            if new_price != '-':
                update_query += "Price = %s, "
                update_data.append(new_price)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the product to update
            update_query += " WHERE ProductID = %s"
            update_data.append(str(product_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Product data updated successfully!")

        else:
            print("ProductID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def brand_exists(cursor, brand_id):
    # Check if the BrandID exists in the brand table
    query_brand = "SELECT BrandID FROM brand WHERE BrandID = %s"
    cursor.execute(query_brand, (brand_id,))
    return cursor.fetchone() is not None

def category_exists(cursor, category_id):
    # Check if the CategoryID exists in the category table
    query_category = "SELECT CategoryID FROM category WHERE CategoryID = %s"
    cursor.execute(query_category, (category_id,))
    return cursor.fetchone() is not None

import mysql.connector
from dbconnection import get_database_connection

def view_product_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the product table
        query_product = "SELECT * FROM product"
        cursor.execute(query_product)

        # Fetch all rows
        product_data = cursor.fetchall()

        if not product_data:
            print("No data found in the product table.")
            return

        # Display header
        print("\nProduct Table:")
        print("| {:<12} | {:<12} | {:<12} | {:<30} | {:<10} |".format("ProductID", "BrandID", "CategoryID", "ProductName", "Price"))
        print("-" * 80)

        # Display data
        for row in product_data:
            product_id, brand_id, category_id, product_name, price = row
            # Replace newline characters with spaces in ProductName
            product_name = product_name.replace('\n', ' ')
            print("| {:<12} | {:<12} | {:<12} | {:<30} | {:<10} |".format(product_id, brand_id, category_id, product_name, price))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()




