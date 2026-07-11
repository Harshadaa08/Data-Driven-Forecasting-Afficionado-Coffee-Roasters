import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Afficionado Coffee Roasters Dashboard",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Data-Driven Forecasting & Demand Prediction")
st.subheader("Afficionado Coffee Roasters")

# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_excel(
        "Afficionado Coffee Roasters.xlsx",
        sheet_name="Transactions"
    )

    df["Revenue"] = df["transaction_qty"] * df["unit_price"]
   # Extract Hour from transaction_time
df["Hour"] = pd.to_datetime(
    df["transaction_time"].astype(str),
    format="%H:%M:%S"
).dt.hour

    return df

df = load_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Filters")

stores = ["All"] + sorted(df["store_location"].unique().tolist())

selected_store = st.sidebar.selectbox(
    "Select Store",
    stores
)

if selected_store != "All":
    df = df[df["store_location"] == selected_store]

# -----------------------------
# KPI Cards
# -----------------------------
total_revenue = df["Revenue"].sum()
total_transactions = df["transaction_id"].count()
total_quantity = df["transaction_qty"].sum()

c1, c2, c3 = st.columns(3)

c1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
c2.metric("🧾 Transactions", f"{total_transactions:,}")
c3.metric("📦 Quantity Sold", f"{total_quantity:,}")

st.divider()

# -----------------------------
# Revenue by Store
# -----------------------------
st.subheader("Revenue by Store")

store_rev = (
    df.groupby("store_location")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
store_rev.plot(kind="bar", ax=ax)
ax.set_ylabel("Revenue")
ax.set_xlabel("Store")
st.pyplot(fig)

# -----------------------------
# Product Category
# -----------------------------
st.subheader("Revenue by Product Category")

cat_rev = (
    df.groupby("product_category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
cat_rev.plot(kind="bar", ax=ax)
ax.set_ylabel("Revenue")
st.pyplot(fig)

# -----------------------------
# Hourly Revenue
# -----------------------------
st.subheader("Hourly Revenue")

hourly = (
    df.groupby("Hour")["Revenue"]
    .sum()
)

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(hourly.index, hourly.values, marker="o")
ax.set_xlabel("Hour")
ax.set_ylabel("Revenue")
ax.grid(True)
st.pyplot(fig)

# -----------------------------
# Heatmap
# -----------------------------
st.subheader("Store-wise Hourly Revenue Heatmap")

heatmap = df.pivot_table(
    values="Revenue",
    index="Hour",
    columns="store_location",
    aggfunc="sum",
    fill_value=0
)

fig, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    heatmap,
    cmap="YlOrRd",
    ax=ax
)

st.pyplot(fig)

# -----------------------------
# Top Products
# -----------------------------
st.subheader("Top 10 Products")

top_products = (
    df.groupby("product_detail")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_products)

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(df.head())

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "Developed by **Harshada R. Kanse** | MBA (Business Analytics & Marketing)"
)
