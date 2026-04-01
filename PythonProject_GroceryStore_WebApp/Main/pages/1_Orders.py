import streamlit as st
from utils.products import get_products
from utils.orders import insert_order

st.title("🧾 Create Order")

# Load products
products = get_products()
product_dict = {p["name"]: p for p in products}

# Initialize session state
if "order_items" not in st.session_state:
    st.session_state.order_items = []

# Customer input
customer_name = st.text_input("Customer Name")

st.subheader("➕ Add Products")

col1, col2 = st.columns(2)

with col1:
    product_name = st.selectbox("Select Product", list(product_dict.keys()))

with col2:
    quantity = st.number_input("Quantity", min_value=1, step=1)

# Add item button
if st.button("Add Item"):
    product = product_dict[product_name]
    
    item = {
        "product_id": product["product_id"],
        "name": product_name,
        "quantity": quantity,
        "price": product["price_per_unit"],
        "total_price": product["price_per_unit"] * quantity
    }

    st.session_state.order_items.append(item)

# Display current order
st.subheader("🛒 Order Summary")

total_amount = 0

for i, item in enumerate(st.session_state.order_items):
    col1, col2, col3, col4 = st.columns(4)

    col1.write(item["name"])
    col2.write(item["quantity"])
    col3.write(f"₹{item['price']}")
    col4.write(f"₹{item['total_price']}")

    total_amount += item["total_price"]

st.markdown(f"### 💰 Total: ₹{total_amount}")

# Place order
if st.button("Place Order"):
    if not customer_name:
        st.error("Please enter customer name")
    elif not st.session_state.order_items:
        st.error("Please add at least one product")
    else:
        insert_order(customer_name, st.session_state.order_items)
        st.success("✅ Order placed successfully!")

        # Clear order
        st.session_state.order_items = []