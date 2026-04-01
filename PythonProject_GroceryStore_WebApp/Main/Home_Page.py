# import streamlit as st

# st.set_page_config(page_title="Grocery Store", layout="wide")

# st.title("🛒 Grocery Store Management System")

# st.image("homepage.jpg", width="stretch")

# st.markdown("Use the sidebar to navigate between Orders and Products.")

import streamlit as st

st.set_page_config(page_title="Raj A-Z Grocery Store", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #2E86C1;
        }
        .sub-text {
            font-size: 18px;
            color: #555;
        }
        .card {
            padding: 20px;
            border-radius: 12px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛒 Grocery Store Management System</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-text">Manage your orders and products efficiently</div>', unsafe_allow_html=True)

st.write("")

# Banner Image
st.image("homepage.jpg", width="stretch")

st.write("")

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h3>📦 Products</h3>
            <p>Manage inventory, prices, and availability</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h3>🧾 Orders</h3>
            <p>Create and track customer orders easily</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h3>📊 Insights</h3>
            <p>View totals and sales performance</p>
        </div>
    """, unsafe_allow_html=True)

st.write("")

st.info("👉 Use the sidebar to navigate between Orders and Products.")

st.sidebar.title("📌 Navigation")
st.sidebar.success("Select a page above")

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", "120")
col2.metric("Revenue", "₹45,000")
col3.metric("Products", "35")

if st.button("🧾 Go to Orders"):
    st.switch_page("pages/1_Orders.py")