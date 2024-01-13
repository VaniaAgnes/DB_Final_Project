import mysql.connector

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="dbproject",
        password="12345678",
        database="dbgrocery"
    )
