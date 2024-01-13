import mysql.connector
from dbconnection import get_database_connection

def authenticate_employee(employee_id):

        connection = get_database_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to check if the employee ID exists
        query = "SELECT * FROM employee WHERE EmployeeID = %s"
        cursor.execute(query, (employee_id,))

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return result is not None  # True if employee ID exists, False otherwise


def create_employee():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        print()
        print("Create Employee:")

        # Get other employee details from the user
        new_employee_id = input("Enter Employee ID for the new employee: ")
        employee_name = input("Enter Employee Name: ")
        position = input("Enter Position: ")
        contact_info = input("Enter Contact Information: ")

        # Execute a query to insert the new employee into the database
        query = "INSERT INTO employee (EmployeeID, EmployeeName, Position, ContactInformation) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (new_employee_id, employee_name, position, contact_info))

        # Commit the changes
        connection.commit()
        
        cursor.close()
        connection.close()

        print("Employee created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_employee():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        print()
        print("Delete Employee:")

        # Get input for brand deletion
        employee_id = input("Enter Employee ID to delete: ")

        # Check if EmployeeID exists
        query_employee = "SELECT EmployeeID FROM employee WHERE EmployeeID = %s"
        cursor.execute(query_employee, (employee_id,))
        employee_result = cursor.fetchone()

        # Execute a query to delete the employee from the database
        if employee_result:
            delete_query = "DELETE FROM employee WHERE EmployeeID = %s"
            cursor.execute(delete_query, (employee_id,))

            # Commit the changes
            connection.commit()

            print("Employee deleted successfully!")

        else:
            print("EmployeeID does not exist. Deletion canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
            
def update_employee():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        print()
        print("Update Employee:")

        # Get input for employee update
        employee_id = input("Enter Employee ID to update: ")

        # Check if EmployeeID exists
        query_employee = "SELECT * FROM employee WHERE EmployeeID = %s"
        cursor.execute(query_employee, (employee_id,))
        employee_result = cursor.fetchone()

        if employee_result:
            print()
            print("Current Employee Data:")
            print("EmployeeID:", employee_result[0])
            print("Employee Name:", employee_result[1])
            print("Position:", employee_result[2])
            print("ContactInformation:", employee_result[3])
            
            print()
            # Get input for updating employee details
            new_employee_name = input("Enter new Employee Name (- to skip): ")
            new_position = input("Enter new Position (- to skip): ")
            new_contactinformation = input("Enter new Contact Information (- to skip): ")
        

            # Prepare the UPDATE query based on user input
            update_query = "UPDATE employee SET "
            update_data = []

            if new_employee_name != '-':
                update_query += "EmployeeName = %s, "
                update_data.append(new_employee_name)

            if new_position != '-':
                update_query += "Position = %s, "
                update_data.append(new_position)

            if new_contactinformation != '-':
                update_query += "ContactInformation = %s, "
                update_data.append(new_contactinformation)


            # Remove the trailing comma and space
            update_query = update_query.rstrip(', ')

            # Add the WHERE clause to specify the employee to update
            update_query += " WHERE EmployeeID = %s"
            update_data.append(str(employee_id))

            # Execute the UPDATE query
            cursor.execute(update_query, tuple(update_data))

            # Commit the changes
            connection.commit()

            print("Employee data updated successfully!")

        else:
            print("EmployeeID does not exist. Update canceled.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()


def view_employee_table():
    try:
        # Get a database connection
        connection = get_database_connection()

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a query to retrieve data from the employee table
        query_employee = "SELECT * FROM employee"
        cursor.execute(query_employee)

        # Fetch all rows
        employee_data = cursor.fetchall()

        if not employee_data:
            print("No data found in the employee table.")
            return

        # Display header
        print("\nEmployee Table:")
        print("| {:<10} | {:<30} | {:<20} | {:<30} |".format("EmployeeID", "EmployeeName", "Position", "ContactInformation"))
        print("-" * 95)

        # Display data
        for row in employee_data:
            print("| {:<10} | {:<30} | {:<20} | {:<30} |".format(row[0], row[1], row[2], row[3]))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            # Close cursor and connection
            cursor.close()
            connection.close()
   