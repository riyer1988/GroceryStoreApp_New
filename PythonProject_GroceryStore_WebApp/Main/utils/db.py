import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RootSQLPass@",
        database="grocery_store"
    )