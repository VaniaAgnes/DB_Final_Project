import mysql.connector
from dbconnection import get_database_connection

def create_category():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        print()
        print("Create Category:")

        # Get other category details from the user
        category_id = input("Enter Category ID for the new category: ")
        category_name = input("Enter Category Name: ")
        category_details = input("Enter Details for this category: ")
        

        # Execute a query to insert the new category into the database
        query = "INSERT INTO category (CategoryID, CategoryName, CategoryDetails) VALUES (%s, %s, %s)"
        cursor.execute(query, (category_id, category_name, category_details))

        # Commit the changes
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Category created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def delete_category():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Delete Category:")

        # Get input for category deletion
        category_id = input("Enter Category ID to delete: ")

        # Check if CategoryID exists
        query_category = "SELECT CategoryID FROM category WHERE CategoryID = %s"
        cursor.execute(query_category, (category_id,))
        category_result = cursor.fetchone()

        # Execute a query to delete the category from the database
        if category_result:
            delete_query = "DELETE FROM category WHERE CategoryID = %s"
            cursor.execute(delete_query, (category_id,))

            # Commit the changes
            connection.commit()

            print("Category deleted successfully!")

        else:
            print("CategoryID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            
            
def update_category():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Category:")

        # Get input for category update
        category_id = input("Enter Category ID to update: ")

        # Check if CategoryID exists
        query_category = "SELECT * FROM category WHERE CategoryID = %s"
        cursor.execute(query_category, (category_id,))
        category_result = cursor.fetchone()

        if category_result:
            print()
            print("Current Category Data:")
            print("CategoryID:", category_result[0])
            print("Category Name:", category_result[1])
            print("Category Details:", category_result[2])
            # Add other columns as needed

            print()
            # Get input for updating category details
            new_category_name = input("Enter new Category Name (- to skip): ")
            new_category_details = input("Enter new Category Details (- to skip): ")
            # Add other variables for additional columns as needed

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE category SET "
            update_data = []

            if new_category_name != '-':
                update_query += "CategoryName = %s, "
                update_data.append(new_category_name)

            if new_category_details != '-':
                update_query += "CategoryDetails = %s, "
                update_data.append(new_category_details)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the category to update
            update_query += " WHERE CategoryID = %s"
            update_data.append(str(category_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Category data updated successfully!")

        else:
            print("CategoryID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            

def view_category_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the category table
        query_category = "SELECT * FROM category"
        cursor.execute(query_category)

        # Fetch all rows
        category_data = cursor.fetchall()

        if not category_data:
            print("No data found in the category table.")
            return

        # Display header
        print("\nCategory Table:")
        print("| {:<12} | {:<25} | {:<50} |".format("CategoryID", "CategoryName", "CategoryDetails"))
        print("-" * 95)

        # Display data
        for row in category_data:
            category_id, category_name, category_details = row
            # Replace newline characters with spaces in CategoryDetails
            category_details = category_details.replace('\n', ' ')
            print("| {:<12} | {:<25} | {:<50} |".format(category_id, category_name, category_details))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()