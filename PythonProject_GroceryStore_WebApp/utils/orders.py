from utils.db import get_connection

def get_orders():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT o.order_id, o.datetime, o.customer_name, 
           SUM(oi.quantity * oi.total_price) as total
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.order_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data


def insert_order(customer_name, items):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders (customer_name) VALUES (%s)",
        (customer_name,)
    )

    order_id = cursor.lastrowid

    for item in items:
        cursor.execute(
            """INSERT INTO order_items 
            (order_id, product_id, quantity, total_price) 
            VALUES (%s, %s, %s, %s)""",
            (order_id, item["product_id"], item["quantity"], item["total_price"])
        )

    conn.commit()
    conn.close()