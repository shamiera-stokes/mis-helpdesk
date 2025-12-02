# mis-helpdesk
MIS Helpdesk project
# MIS Help Desk Dashboard

## What is this?

This project is a Help Desk Dashboard. It helps a company see all support tickets, who is working on them, and how fast they get solved. It shows the important numbers and charts so managers can understand what’s happening.

---

## Project Files

**Code:**
- `streamlit_app.py` – The main Streamlit app you open in a browser.
- `tickets.db` – The SQLite database with all the ticket info.
- `data_generator.py` – Script to make fake ticket data.
- Any extra Python files your app uses.

**Documents:**
- Process Map PNG + .drawio – Shows ticket workflow.
- ER Diagram PNG + .drawio – Shows database structure.
- Governance Memo PDF – Explains rules and policies.
- Project Overview PDF – Short summary of the project.

---

## Features

- Sidebar filters: choose date range, priority, agent, or status.
- KPI cards: total tickets, median resolution time, SLA breach %.
- Charts: weekly ticket volume (line), tickets by agent/priority (bar).
- Table: see filtered tickets and download CSV.
- About section: explains assumptions and data updates.

---

## How to Use

1. Open the app on **Streamlit Cloud**.
2. Use the **sidebar filters** to see only the tickets you want.
3. Check the **KPIs** at the top to see important numbers.
4. Look at the **charts** to understand trends.
5. Scroll down to the **data table** to see all tickets.
6. Click **Download CSV** to get the ticket data.
7. Read the **About** section to see assumptions and refresh info.
8. import streamlit as st
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



---

## Notes

- All data is fake for practice—no personal info is included.
- Make sure your Streamlit app file is named **`streamlit_app.py`**.
- The dashboard is designed to load quickly and show info clearly.
