import streamlit as st
import pandas as pd
import sqlite3

# -------------------------
# Load data from SQLite
# -------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("tickets.db")
    df = pd.read_sql_query("SELECT * FROM tickets", conn)
    conn.close()
    return df

st.set_page_config(page_title="Helpdesk Dashboard", layout="wide")

st.title("📞 Helpdesk Support Dashboard")

# Load data
df = load_data()

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filter Tickets")

status_filter = st.sidebar.selectbox(
    "Ticket Status",
    options=["All"] + sorted(df["status"].unique().tolist())
)

agent_filter = st.sidebar.selectbox(
    "Assigned Agent",
    options=["All"] + sorted(df["assigned_to"].unique().tolist())
)

priority_filter = st.sidebar.selectbox(
    "Priority",
    options=["All"] + sorted(df["priority"].unique().tolist())
)

# Apply filters
filtered_df = df.copy()

if status_filter != "All":
    filtered_df = filtered_df[filtered_df["status"] == status_filter]

if agent_filter != "All":
    filtered_df = filtered_df[filtered_df["assigned_to"] == agent_filter]

if priority_filter != "All":
    filtered_df = filtered_df[filtered_df["priority"] == priority_filter]

# -------------------------
# KPIs
# -------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tickets", len(filtered_df))

with col2:
    st.metric("Open Tickets", sum(filtered_df["status"] == "Open"))

with col3:
    st.metric("Closed Tickets", sum(filtered_df["status"] == "Closed"))

# -------------------------
# Show Data
# -------------------------
st.subheader("📁 Ticket Table")
st.dataframe(filtered_df, use_container_width=True)

