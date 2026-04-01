import streamlit as st
import pandas as pd
from utils.products import get_products, add_product

st.title("Products")

products = get_products()

df = pd.DataFrame(products)
st.dataframe(df)

st.subheader("Add New Product")

name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)
uom_id = st.number_input("UOM ID", min_value=1)

if st.button("Add Product"):
    add_product(name, uom_id, price)
    st.success("Product added!")