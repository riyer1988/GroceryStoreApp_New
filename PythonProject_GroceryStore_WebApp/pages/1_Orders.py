import streamlit as st
import pandas as pd
from utils.orders import get_orders, insert_order
from utils.products import get_products

st.title("Orders")

orders = get_orders()

df = pd.DataFrame(orders)
st.dataframe(df)

st.subheader("Create New Order")

customer_name = st.text_input("Customer Name")

products = get_products()
product_options = {p["name"]: p["product_id"] for p in products}

selected_product = st.selectbox("Select Product", list(product_options.keys()))
quantity = st.number_input("Quantity", min_value=1)

if st.button("Add Order"):
    if not customer_name:
        st.error("Customer name is required")
    else:
        product_id = product_options[selected_product]
        total_price = quantity * 10  # replace with real price later

        insert_order(customer_name, [{
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        }])

        st.success("Order created successfully!")