# from utils.db import get_connection

# def get_orders():
#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)

#     query = """
#     SELECT o.order_id, o.datetime, o.customer_name, 
#            SUM(oi.quantity * oi.total_price) as total
#     FROM orders o
#     JOIN order_items oi ON o.order_id = oi.order_id
#     GROUP BY o.order_id
#     """

#     cursor.execute(query)
#     data = cursor.fetchall()

#     conn.close()
#     return data


# def insert_order(customer_name, items):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO orders (customer_name) VALUES (%s)",
#         (customer_name,)
#     )

#     order_id = cursor.lastrowid

#     for item in items:
#         cursor.execute(
#             """INSERT INTO order_items 
#             (order_id, product_id, quantity, total_price) 
#             VALUES (%s, %s, %s, %s)""",
#             (order_id, item["product_id"], item["quantity"], item["total_price"])
#         )

#     conn.commit()
#     conn.close()

from utils.db import get_connection


def get_orders():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT o.order_id, o.datetime, o.customer_name, 
           SUM(oi.quantity * oi.total_price) as total
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.order_id, o.datetime, o.customer_name
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


from utils.db import get_connection


def insert_order(customer_name, items):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert into orders
        cursor.execute(
            "INSERT INTO orders (customer_name) VALUES (%s)",
            (customer_name,)
        )

        order_id = cursor.lastrowid

        # Insert multiple items
        for item in items:
            cursor.execute(
                """
                INSERT INTO order_items 
                (order_id, product_id, quantity, total_price) 
                VALUES (%s, %s, %s, %s)
                """,
                (
                    order_id,
                    item["product_id"],
                    item["quantity"],
                    item["total_price"],
                )
            )

        # Update total
        cursor.execute(
            """
            UPDATE orders
            SET total = (
                SELECT SUM(quantity * total_price)
                FROM order_items
                WHERE order_id = %s
            )
            WHERE order_id = %s
            """,
            (order_id, order_id)
        )

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()