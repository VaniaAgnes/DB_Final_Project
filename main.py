import mysql.connector
from dbconnection import get_database_connection
from employee import create_employee, authenticate_employee, delete_employee, update_employee, view_employee_table
from brand import create_brand, delete_brand, update_brand, view_brand_table
from category import create_category, delete_category, update_category, view_category_table
from product import create_product, delete_product, update_product, view_product_table
from transaction import create_transaction, delete_transaction, update_salestransaction, view_transaction_table
from purchased import update_itempurchased, view_item_purchased_table
from inventory import create_inventory, delete_inventory, update_inventory, view_inventory_table
from Query import *
    
def main_menu():
    print("\nMain Menu:")
    print("1. Employee Function")
    print("2. Brand Function")
    print("3. Category Function")
    print("4. Product Function")
    print("5. Transaction Function")
    print("6. Purchased Function")
    print("7. Inventory Function")
    print("8. List of Queries")
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

def query_menu():
    print("List of Queries Menu:")
    print("1. Check the Total Purchased Quantity for Each Brand")
    print("2. Find Products with Low Quantities")
    print("3. Retrieve the Latest Restock Dates for Each Product")
    print("4. Retrieve a List of Sales Transactions for a Specific Day")
    print("5. Find Products That Have No Sales")
    print("6. Get the Total Revenue for Each Category")
    print("7. Average Transaction Amount (in Rupiah)")
    print("8. Total Sales Transactions by Date (does not include unsuccessful transaction)")
    print("9. Check the Account Mutations Within a Specified Period")
    print("10. Retrieve the Brand with The Most Sales")
    print("11. Back to Main Menu")

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

            choice = input("Enter your choice (0-8): ")

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
                            delete_inventory()

                        elif inventory_choice == "3":
                            update_inventory()

                        elif inventory_choice == "4":
                            view_inventory_table()

                        elif inventory_choice == "5":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please try again.")
            
            elif choice == '8':
                    while True:
                        print()
                        query_menu()
                        query_choice = input("Enter your choice: ")

                        if query_choice == "1":
                            total_purchased_brand()

                        elif query_choice == "2":
                            product_low_quantity()

                        elif query_choice == "3":
                            retrieve_latest_restock()

                        elif query_choice == "4":
                            date_str = input("Enter the date (YYYY-MM-DD): ")
                            retrieve_transaction_on_specificDay(date_str)

                        elif query_choice == "5":
                            no_sale_products()

                        elif query_choice == "6":
                            get_total_revenue_cat()

                        elif query_choice == "7":
                            average_transaction_amount()

                        elif query_choice == "8":
                            total_transactions_by_date()

                        elif query_choice == "9":
                            start_date_str = input("Enter the beginning date (YYYY-MM-DD): ")
                            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
                            check_mutations(start_date_str, end_date_str)

                        elif query_choice == "10":
                            brand_most_sales()

                        elif query_choice == "11":
                            print("Returning to the main menu...")
                            break

                        else:
                            print("That is not part of our queries. Please try again.")

            elif choice == "0":
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 0 and 7.")


if __name__ == "__main__":
    main()