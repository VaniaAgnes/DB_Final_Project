import mysql.connector
from dbconnection import get_database_connection
from purchased import create_item_purchased

def create_transaction():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Create Transaction:")

        # Get other transaction details from the user
        transaction_id = input("Enter Transaction ID for the new transaction: ")
        trans_employee_id = input("Enter Employee ID for the new transaction: ")
        transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")
        total_amount = input("Enter Total Amount: ")
        payment_status = input("Enter Payment Status (Successful / Unsuccessful):")
    
        # Check if EmployeeID exists
        query_employee = "SELECT EmployeeID FROM employee WHERE EmployeeID = %s"
        cursor.execute(query_employee, (trans_employee_id,))
        employee_result = cursor.fetchone()

        # Execute a query to insert the new transaction into the database
        if employee_result:
            query = "INSERT INTO salestransaction (TransactionID, EmployeeID, TransactionDate, TotalAmount, PaymentStatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (transaction_id, trans_employee_id, transaction_date, total_amount, payment_status))

            # Commit the changes
            connection.commit()

            cursor.close()
            connection.close()

            print("Transaction created successfully!")
            print()
            print("Please insert the products for this transaction !")
            print()
            create_item_purchased(transaction_id)

        else:
            print("EmployeeID does not exist. Transaction creation canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def delete_transaction():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Delete Transaction:")

        # Get input for transaction deletion
        transaction_id = input("Enter Transaction ID to delete: ")

        # Check if TransactionID exists
        query_transaction = "SELECT TransactionID FROM salestransaction WHERE TransactionID = %s"
        cursor.execute(query_transaction, (transaction_id,))
        transaction_result = cursor.fetchone()

        # Execute a query to delete the transaction and associated item purchases from the database
        if transaction_result:
            # Delete associated item purchases first
            delete_query_itempurchased = "DELETE FROM itempurchased WHERE TransactionID = %s"
            cursor.execute(delete_query_itempurchased, (transaction_id,))

            # Delete the transaction
            delete_query_transaction = "DELETE FROM salestransaction WHERE TransactionID = %s"
            cursor.execute(delete_query_transaction, (transaction_id,))

            # Commit the changes
            connection.commit()

            print("Transaction and associated item purchases deleted successfully!")

        else:
            print("TransactionID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()


def update_salestransaction():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Sales Transaction:")

        # Get input for sales transaction update
        transaction_id = input("Enter Transaction ID to update: ")

        # Check if TransactionID exists
        query_transaction = "SELECT * FROM salestransaction WHERE TransactionID = %s"
        cursor.execute(query_transaction, (transaction_id,))
        transaction_result = cursor.fetchone()

        if transaction_result:
            print()
            print("Current Sales Transaction Data:")
            print("TransactionID:", transaction_result[0])
            print("Employee ID:", transaction_result[1])
            print("Transaction Date:", transaction_result[2])
            print("Total Amount:", transaction_result[3])
            print("Payment Status:", transaction_result[4])
            # Add other columns as needed

            print()
            # Get input for updating sales transaction details
            new_employee_id = input("Enter new Employee ID (- to skip): ")
            new_transaction_date = input("Enter new Transaction Date (YYYY-MM-DD, - to skip): ")
            new_total_amount = input("Enter new Total Amount (- to skip): ")
            new_payment_status = input("Enter new Payment Status (- to skip): ")
            # Add other variables for additional columns as needed

            # Check if the new EmployeeID exists
            if new_employee_id != '-' and not employee_exists(cursor, new_employee_id):
                print("Employee ID does not exist. Update canceled.")
                return

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE salestransaction SET "
            update_data = []

            if new_employee_id != '-':
                update_query += "EmployeeID = %s, "
                update_data.append(new_employee_id)

            if new_transaction_date != '-':
                update_query += "TransactionDate = %s, "
                update_data.append(new_transaction_date)

            if new_total_amount != '-':
                update_query += "TotalAmount = %s, "
                update_data.append(new_total_amount)

            if new_payment_status != '-':
                update_query += "PaymentStatus = %s, "
                update_data.append(new_payment_status)

            # Add other conditions for additional columns as needed

            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the transaction to update
            update_query += " WHERE TransactionID = %s"
            update_data.append(str(transaction_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Sales transaction data updated successfully!")

        else:
            print("TransactionID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()

def employee_exists(cursor, employee_id):
    # Check if the EmployeeID exists in the employee table
    query_employee = "SELECT EmployeeID FROM employee WHERE EmployeeID = %s"
    cursor.execute(query_employee, (employee_id,))
    return cursor.fetchone() is not None


def view_transaction_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the salestransaction table
        query_transaction = "SELECT * FROM salestransaction"
        cursor.execute(query_transaction)

        # Fetch all rows
        transaction_data = cursor.fetchall()

        if not transaction_data:
            print("No data found in the salestransaction table.")
            return

        # Display header
        print("\nTransaction Table:")
        print("| {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format("TransactionID", "EmployeeID", "TransactionDate", "TotalAmount", "PaymentStatus"))
        print("-" * 80)

        # Display data
        for row in transaction_data:
            transaction_id, employee_id, transaction_date, total_amount, payment_status = row
            formatted_date = transaction_date.strftime('%Y-%m-%d') if transaction_date else ''
            print("| {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |".format(transaction_id, employee_id, formatted_date, total_amount, payment_status))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()



           
    
   