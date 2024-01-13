import mysql.connector
from dbconnection import get_database_connection
from employee import create_employee, authenticate_employee, delete_employee, update_employee, view_employee_table
from brand import create_brand, delete_brand, update_brand, view_brand_table
from category import create_category, delete_category, update_category, view_category_table
from product import create_product, delete_product, update_product, view_product_table
from transaction import create_transaction, delete_transaction, update_salestransaction, view_transaction_table
from purchased import update_itempurchased, view_item_purchased_table
from inventory import create_inventory, delete_inventory, update_inventory, view_inventory_table

    
def main_menu():
    print("\nMain Menu:")
    print("1. Employee Function")
    print("2. Brand Function")
    print("3. Category Function")
    print("4. Product Function")
    print("5. Transaction Function")
    print("6. Purchased Function")
    print("7. Inventory Function")
    print("0. Exit")
    
def employee_menu():
    print("Employee Menu:")
    print("1. Create Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. See Employee List")
    print("5. Back to Main Menu")
    
def brand_menu():
    print("Brand Menu:")
    print("1. Create Brand")
    print("2. Delete Brand")
    print("3. Update Brand")
    print("4. See Brand List")
    print("5. Back to Main Menu")
    
def category_menu():
    print("Category Menu:")
    print("1. Create Category")
    print("2. Delete Category")
    print("3. Update Category")
    print("4. See Category List")
    print("5. Back to Main Menu")
    
def product_menu():
    print("Product Menu:")
    print("1. Create Product")
    print("2. Delete Product")
    print("3. Update Product")
    print("4. See Product List")
    print("5. Back to Main Menu")
    
def transaction_menu():
    print("Transaction Menu:")
    print("1. Create Transaction and Item Purchased")
    print("2. Delete Transaction and Item Purchased")
    print("3. Update Transaction")
    print("4. See Transaction List")
    print("5. Back to Main Menu")
    
def purchased_menu():
    print("Purchased Menu:")
    print("1. Update Item Purchased")
    print("2. See Item Purchased List")
    print("3. Back to Main Menu")
    
def inventory_menu():
    print("Inventory Menu:")
    print("1. Create Inventory")
    print("2. Delete Inventory")
    print("3. Update Inventory")
    print("4. See Inventory List")
    print("5. Back to Main Menu")
    

def main():
    # Get employee ID from the user
    employee_id = input("Enter your employee ID: ")

    # Authenticate the employee
    if authenticate_employee(employee_id):
        print("Authentication successful!")
        print()
        print("Welcome to Grocery Management System ⋆｡ﾟ 🛒｡ﾟ｡⋆ !  ")
        while True:
            main_menu()

            choice = input("Enter your choice (0-7): ")

            if choice == "1":
                while True:
                    print()
                    employee_menu()
                    employee_choice = input("Enter your choice: ")

                    if employee_choice == "1":
                        create_employee()

                    elif employee_choice == "2":
                        delete_employee()
    
                    elif employee_choice == "3":
                        update_employee()

                    elif employee_choice == "4":
                        view_employee_table()

                    elif employee_choice == "5":
                        print("Returning to the main menu...")
                        break
                        

                    else:
                        print("Invalid choice. Please try again.")

            # Add other choices for different functions as needed
            elif choice == "2":
                    while True:
                        print()
                        brand_menu()
                        brand_choice = input("Enter your choice: ")

                        if brand_choice == "1":
                            create_brand()

                        elif brand_choice == "2":
                            delete_brand()
                            
                        elif brand_choice == "3":
                            update_brand()

                        elif brand_choice == "4":
                            view_brand_table()

                        elif brand_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")


            elif choice == "3":
                    while True:
                        print()
                        category_menu()
                        category_choice = input("Enter your choice: ")

                        if category_choice == "1":
                            create_category()
                            
                        elif category_choice == "2":
                            delete_category()
                            
                        elif category_choice == "3":
                            update_category()

                        elif category_choice == "4":
                            view_category_table()

                        elif category_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")
                            
            elif choice == "4":
                    while True:
                        print()
                        product_menu()
                        product_choice = input("Enter your choice: ")

                        if product_choice == "1":
                            create_product()

                        elif product_choice == "2":
                            delete_product()

                        elif product_choice == "3":
                            update_product()

                        elif product_choice == "4":
                            view_product_table()

                        elif product_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")

            elif choice == "5":
                    while True:
                        print()
                        transaction_menu()
                        transaction_choice = input("Enter your choice: ")

                        if transaction_choice == "1":
                            create_transaction()

                        elif transaction_choice == "2":
                            delete_transaction()

                        elif transaction_choice == "3":
                            update_salestransaction()

                        elif transaction_choice == "4":
                            view_transaction_table()

                        elif transaction_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")

            elif choice == "6":
                    while True:
                        print()
                        purchased_menu()
                        purchased_choice = input("Enter your choice: ")

                        if purchased_choice == "1":
                            update_itempurchased()

                        elif purchased_choice == "2":
                            view_item_purchased_table()

                        elif purchased_choice == "3":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")

            elif choice == "7":
                    while True:
                        print()
                        inventory_menu()
                        inventory_choice = input("Enter your choice: ")

                        if inventory_choice == "1":
                            create_inventory()
                            
                        elif inventory_choice == "2":
                            delete_inventory

                        elif inventory_choice == "3":
                            update_inventory()

                        elif inventory_choice == "4":
                            view_inventory_table()

                        elif inventory_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")
            
            
            
            elif choice == "0":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 0 and 7.")


if __name__ == "__main__":
    main()