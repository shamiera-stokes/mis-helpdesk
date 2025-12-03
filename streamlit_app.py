Collecting streamlit
  Downloading streamlit-1.51.0-py3-none-any.whl.metadata (9.5 kB)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.2)
Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.1)
Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow<22,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.12.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.11.12)
Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.37.0)
Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.29.0)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)
Downloading streamlit-1.51.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 71.1 MB/s eta 0:00:00
Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 105.4 MB/s eta 0:00:00
Installing collected packages: pydeck, streamlit
Successfully installed pydeck-0.9.1 streamlit-1.51.0

[18]
0s
%%writefile app.py
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

DB_PATH = "data/tickets.db"

# ----------------------
# Page config

Writing app.py

[19]
0s
# Kill any old Streamlit processes (just in case)
!pkill -f streamlit 2>/dev/null || echo "no old streamlit"

# Start Streamlit app in the background
!streamlit run app.py --server.address 0.0.0.0 --server.port 8501 &>/dev/null &
print("Streamlit started on port 8501")

^C
Streamlit started on port 8501

[20]
8s
!streamlit run app.py --server.address 0.0.0.0 --server.port 8501


Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.

2025-12-03 04:56:27.663 Port 8501 is already in use

[21]
0s
import os, textwrap

# 1) Make sure the src folder exists
os.makedirs("src", exist_ok=True)

# 2) This is the full Streamlit app code
app_code = """
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

DB_PATH = "data/tickets.db"

# -------- LOAD DATA --------
@st.cache_data
def load_data():
    con = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM tickets", con)
    con.close()

    # Convert timestamp columns
    for col in ["created_at", "first_response_at", "resolved_at"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Helper columns
    df["resolution_hours"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600
    df["week_start"] = df["created_at"].dt.to_period("W").apply(lambda r: r.start_time)
    df["sla_breached"] = df["resolution_hours"] > 72

    return df

st.set_page_config(page_title="Help Desk IS Dashboard", layout="wide")
st.title("📊 Help Desk Information System Dashboard")

df = load_data()

# -------- SIDEBAR FILTERS --------
st.sidebar.header("Filters")

min_date = df["created_at"].min().date()
max_date = df["created_at"].max().date()

start_date, end_date = st.sidebar.date_input(
    "Created date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

mask_date = (df["created_at"].dt.date >= start_date) & (df["created_at"].dt.date <= end_date)

priorities = sorted(df["priority"].unique().tolist())
selected_priorities = st.sidebar.multiselect("Priority", priorities, default=priorities)
mask_priority = df["priority"].isin(selected_priorities)

filtered = df[mask_date & mask_priority].copy()

st.sidebar.markdown(f"**Tickets shown:** {len(filtered)}")

# -------- KPIs --------
st.subheader("Key Metrics")

total_tickets = len(filtered)
median_resolution = filtered["resolution_hours"].median()
sla_breach_rate = (filtered["sla_breached"].mean() * 100) if len(filtered) > 0 else 0
backlog = filtered["status"].str.lower().isin(["open", "in progress"]).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tickets", total_tickets)
col2.metric("Median Resolution (hrs)", f"{median_resolution:.1f}" if pd.notna(median_resolution) else "N/A")
col3.metric("SLA Breach Rate", f"{sla_breach_rate:.1f}%")
col4.metric("Backlog", backlog)

st.markdown("---")

# -------- CHARTS --------
st.subheader("Tickets per Week")
weekly_counts = filtered.groupby("week_start")["ticket_id"].count()
st.line_chart(weekly_counts)

st.subheader("Tickets by Priority")
priority_counts = filtered["priority"].value_counts()
st.bar_chart(priority_counts)

st.subheader("Resolution Time Distribution (Hours)")
st.hist(filtered["resolution_hours"].dropna(), bins=30)
"""

# 3) Write it to src/app.py
with open("src/app.py", "w") as f:
    f.write(textwrap.dedent(app_code))

print("Saved app.py:", os.path.exists("src/app.py"))

Saved app.py: True

[22]
18s
!pip install -q streamlit cloudflared

  Preparing metadata (setup.py) ... done
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.0/63.0 kB 2.5 MB/s eta 0:00:00
  Building wheel for cloudflared (setup.py) ... done

[23]
0s
# Download Cloudflare tunnel binary and make it executable
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
!chmod +x cloudflared

print("cloudflared downloaded and ready.")

cloudflared downloaded and ready.

[24]
3s
import re, time, subprocess

print("Starting Cloudflare tunnel...\n")

# Start cloudflared tunnel to the Streamlit app
proc = subprocess.Popen(
    ["./cloudflared", "tunnel", "--url", "http://localhost:8501", "--no-autoupdate"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)

# Read output lines and look for the public URL
public_url = None
for i in range(120):  # check for ~120 seconds
    line = proc.stdout.readline()
    if not line:
        break
    print(line.strip())
    m = re.search(r"https://[a-zA-Z0-9.-]*trycloudflare.com", line)
    if m:
        public_url = m.group(0)
        break

if public_url:
    print("\n🎉 YOUR STREAMLIT HELP DESK URL:")
    print(public_url)
    print("\nClick that link to open your website.")
else:
    print("\n❌ Could not detect Cloudflare URL. Scroll above for any errors.")

Starting Cloudflare tunnel...

2025-12-03T04:56:48Z INF Thank you for trying Cloudflare Tunnel. Doing so, without a Cloudflare account, is a quick way to experiment and try it out. However, be aware that these account-less Tunnels have no uptime guarantee, are subject to the Cloudflare Online Services Terms of Use (https://www.cloudflare.com/website-terms/), and Cloudflare reserves the right to investigate your use of Tunnels for violations of such terms. If you intend to use Tunnels in production you should use a pre-created named tunnel by following: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps
2025-12-03T04:56:48Z INF Requesting new quick Tunnel on trycloudflare.com...
2025-12-03T04:56:51Z INF +--------------------------------------------------------------------------------------------+
2025-12-03T04:56:51Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
2025-12-03T04:56:51Z INF |  https://tribes-ireland-car-tales.trycloudflare.com                                        |

🎉 YOUR STREAMLIT HELP DESK URL:
https://tribes-ireland-car-tales.trycloudflare.com

Click that link to open your website.
Governance Memo

Shamiera Stokes

Date: 11/30/2025

Class: Management Information Sys/Comp (I) BSMG 3310-01

Professor Gray

                              Governance Memo
Government Memorandum To: Information Systems Oversight CommitteeShamiera Stokes Systems AnalystSubject: Data Governance, Security Controls, and Operational Policies for the Help Desk Information SystemDate: 11/30/2025

Purpose The purpose of this memorandum is to outline the data-handling rules, system security decisions, and operational safeguards I implemented while developing the Help Desk Information System (HDIS). Although this project uses simulated data, the structure is modeled on standards that a government or institutional IT department would follow. The intent is to create a system that functions correctly and demonstrates responsible data governance.

Data Protection and Privacy Controls One of the first design priorities was minimizing exposure to sensitive information.To prevent any privacy risks, all records in the system use fully fabricated data—including names, email addresses, timestamps, and ticket descriptions. No real students, faculty, or staff are referenced anywhere in the database. The database schema itself was intentionally limited. It stores only the fields required for ticket management: creation time, status, priority, assignment, category, and update logs. No personal identifiers or unnecessary metadata were included. This “minimum-data” strategy reduces risk and supports easier oversight. If the system were deployed in a real environment, the database would be placed in a secured server environment with role-controlled access and routine integrity checks.

Role-Based Access Structure To maintain operational security, the HDIS uses a three-tier access model: Help Desk Agents

View and update only the tickets assigned to them.
Cannot modify database structure, global settings, or system logs. Supervisors / Managers
Access to all tickets and performance metrics.
Read-only view of system-level information to support planning and oversight. System Administrators
Full technical access.
Responsible for database maintenance, configuration management, and reliability monitoring. This separation ensures that individuals only access what is necessary for their responsibilities.
Backup Strategy and Recovery Planning Technology failures are inevitable, so the HDIS design includes a straightforward backup schedule:
Daily copy of the primary SQLite database.
Weekly full snapshot of the entire project directory.
Timestamped archives to support chronological traceability. If a failure occurs, recovery involves restoring the most recent copy, rebuilding database indexes, and verifying record integrity. Practicing this process—even with fake data—reinforces operational discipline.
Change Management Procedures All system changes follow a structured approval path:

Document the proposed modification.

Test it on a separate environment or cloned database.

Perform a peer or supervisor review.

Deploy the approved change to the production environment.

Record the update in a change log. This reduces the risk of unexpected errors and ensures accountability for every system adjustment.

System Logging and Audit Trails Logging is essential for internal oversight. The HDIS plan includes logs for:

Ticket edits and status updates
Changes to database tables or structure
Data exports or deletions
System errors
Authentication attempts (for future upgrades) SQLite’s write-ahead logging further helps protect data integrity during simultaneous operations.
Planning for Migration to PostgreSQL If the HDIS had to scale to support more users or higher demand, PostgreSQL would be a suitable upgraded database system. Migration would involve: Exporting all records from SQLite Applying minor schema adjustments Importing the data into PostgreSQL Updating the Streamlit connection strings Rebuilding indexes for performance The current design intentionally keeps the structure simple, which makes future migration efficient and manageable.
Conclusion This project goes beyond programming a functional help desk tool. It demonstrates how a real information system must manage privacy, access control, data reliability, and long-term maintainability. Every design choice was made to support secure operation, clear governance, and future scalability.

README.md
MIS Help Desk Information System
**By Shamiera Stokes

MIS Help Desk Dashboard What is this? This project is a Help Desk Dashboard. It helps a company see all support tickets, who is working on them, and how fast they get solved. It shows the important numbers and charts so managers can understand what’s happening.

Project Files Code:

streamlit_app.py – The main Streamlit app you open in a browser. tickets.db – The SQLite database with all the ticket info. data_generator.py – Script to make fake ticket data. Any extra Python files your app uses. Documents:

Process Map PNG + .drawio – Shows ticket workflow. ER Diagram PNG + .drawio – Shows database structure. Governance Memo PDF – Explains rules and policies. Project Overview PDF – Short summary of the project. Features Sidebar filters: choose date range, priority, agent, or status. KPI cards: total tickets, median resolution time, SLA breach %. Charts: weekly ticket volume (line), tickets by agent/priority (bar). Table: see filtered tickets and download CSV. About section: explains assumptions and data updates. How to Use Open the app on Streamlit Cloud. Use the sidebar filters to see only the tickets you want. Check the KPIs at the top to see important numbers. Look at the charts to understand trends. Scroll down to the data table to see all tickets. Click Download CSV to get the ticket data. Read the About section to see assumptions and refresh info. import streamlit as st import pandas as pd import sqlite3

Project Overview
The MIS Helpdesk Project is designed to streamline the process of resolving computer-related issues. Users can submit requests whenever they encounter a problem, and the helpdesk team can efficiently track and address these issues. The system keeps detailed records of each request, including who reported it, who is handling it, and the status of resolution. Additionally, the project provides insights into the frequency of issues and response times, helping to improve overall efficiency. This project not only makes it easier for users to get the help they need but also ensures that all tasks are well-organized and transparent.

Setup Instructions

Clone the repository: Use git clone to get the project on your local machine.

Install dependencies: Run pip install -r requirements.txt to install all necessary packages.

For any issues or questions, please refer to the documentation or contact the development team.

Regular updates and improvements will be made to keep the system efficient and user-friendly.

Project Structure
helpdesk-is/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── tickets.db
│
├── diagrams/
│   ├── process_map.drawio
│   ├── process_map.png
│   ├── erd.drawio
│   └── erd.png
│
├── sql/
│   └── schema.sql
│
├── src/
│   ├── generate_data.ipynb
│   ├── analysis.ipynb
│   └── app.py
│
└── screenshots/
    └── dashboard_images.png (or multiple .png files)
Tools Used
All tools required are free and open-source:

SQLite + DB Browser / DBeaver CE
Python (Pandas, NumPy, Faker)
Jupyter / Google Colab
Matplotlib
Streamlit
diagrams.net (draw.io)
GitHub
Database
The system uses a SQLite file named tickets.db inside the data/ folder.

Tables include:

tickets
agents
customers
ticket_updates
Lookup fields (priority, status, channel)
All data is synthetic and follows rules like realistic timestamps, SLA logic, and possible ticket re-opens.

Analytics Notebook
Located in:

src/analysis.ipynb
The analytics includes:

Weekly ticket volume

Average and median resolution times

SLA breach percentage

Backlog counts

Ticket counts by priority and agent

Three visuals:

Line chart: Tickets per Week
Bar chart: Tickets by Priority
Histogram: Resolution Hours
Interpretations for each result are included.

Streamlit App
Located in:

src/app.py
The app includes:

Date range filter
Priority filter
Status filter
Agent filter
KPI cards
Line chart (tickets per week)
Bar charts (priority and agent)
Downloadable CSV
Ticket table
“About this dashboard” section
Subtitle: Built by Shamiera Stokes
To run locally:

streamlit run src/app.py
Governance Summary
A full governance memo (PDF) is included separately. It covers:

Synthetic data and privacy
Role-based access
Backup and restore expectations
Logging and monitoring
Path to scale into PostgreSQL
How to Run the Project
Clone the repo

Install requirements:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run src/app.py
Open the dashboard in your browser to explore all filters, KPIs, and visuals.

Screenshots
Screenshot 1 – Dashboard KPIs

Screenshot 2 – Tickets by Agent

Screenshot 3 – Ticket Table

Screenshot 2025-11-27 at 3.24.20 AM.pngScreenshot 2025-11-27 at 3.24.08 AM.pngScreenshot 2025-11-27 at 3.23.31 AM.png

Colab paid products - Cancel contracts here
