import mysql.connector
from dbconnection import get_database_connection

def create_brand():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        print()
        print("Create Brand:")

        # Get other brand details from the user
        brand_id = input("Enter Brand ID for the new brand: ")
        brand_name = input("Enter Brand Name: ")
        

        # Execute a query to insert the new brand into the database
        query = "INSERT INTO brand (BrandID, BrandName) VALUES (%s, %s)"
        cursor.execute(query, (brand_id, brand_name))

        # Commit the changes
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Brand created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

def delete_brand():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        print()
        print("Delete Brand:")

        # Get input for brand deletion
        brand_id = input("Enter Brand ID to delete: ")

        # Check if BrandID exists
        query_brand = "SELECT BrandID FROM brand WHERE BrandID = %s"
        cursor.execute(query_brand, (brand_id,))
        brand_result = cursor.fetchone()

        # Execute a query to delete the brand from the database
        if brand_result:
            delete_query = "DELETE FROM brand WHERE BrandID = %s"
            cursor.execute(delete_query, (brand_id,))

            # Commit the changes
            connection.commit()

            print("Brand deleted successfully!")

        else:
            print("BrandID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            

def update_brand():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Brand:")

        # Get input for brand update
        brand_id = input("Enter Brand ID to update: ")

        # Check if BrandID exists
        query_brand = "SELECT * FROM brand WHERE BrandID = %s"
        cursor.execute(query_brand, (brand_id,))
        brand_result = cursor.fetchone()

        if brand_result:
            print()
            print("Current Brand Data:")
            print("BrandID:", brand_result[0])
            print("Brand Name:", brand_result[1])
            # Add other columns as needed

            print()
            # Get input for updating brand details
            new_brand_name = input("Enter new Brand Name (- to skip): ")
            # Add other variables for additional columns as needed

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE brand SET "
            update_data = []

            if new_brand_name != '-':
                update_query += "BrandName = %s, "
                update_data.append(new_brand_name)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the brand to update
            update_query += " WHERE BrandID = %s"
            update_data.append(str(brand_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Brand data updated successfully!")

        else:
            print("BrandID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def view_brand_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the brand table
        query_brand = "SELECT * FROM brand"
        cursor.execute(query_brand)

        # Fetch all rows
        brand_data = cursor.fetchall()

        if not brand_data:
            print("No data found in the brand table.")
            return

        # Display header
        print("\nBrand Table:")
        print("| {:<10} | {:<30} |".format("BrandID", "BrandName"))
        print("-" * 43)

        # Display data
        for row in brand_data:
            print("| {:<10} | {:<30} |".format(row[0], row[1]))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()


