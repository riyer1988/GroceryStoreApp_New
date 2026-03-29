from utils.db import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    conn.close()
    return data


def add_product(name, uom_id, price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)",
        (name, uom_id, price)
    )

    conn.commit()
    conn.close()