# DB Monitoring System

A simple PostgreSQL database monitoring tool for beginner DBAs. This script performs:

- ✅ Database health check
- 📊 Daily sales quantity summary
- 🚨 Alerts for unusually high sales
- 📈 Alerts if table grows too large

---

## 🔧 Tech Stack

- Language: Python
- DB: PostgreSQL
- Library: `psycopg2`

---

## 📁 Project Structure

db-monitoring-system/
├── sql/
│ └── schema.sql
├── scripts/
│ └── monitor_db.py
├── logs/
│ └── monitor_log.log
├── cron_job.txt
└── README.md


---

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/AkashDevX/db-monitoring-system.git
cd db-monitoring-system

    Install dependencies:

pip install psycopg2

    Set up PostgreSQL using sql/schema.sql.

    Run the script:

python scripts/monitor_db.py

🕒 Automate with CRON (or Windows Task Scheduler)

    Example CRON (Linux/macOS):

0 9 * * * python /path/to/your/project/scripts/monitor_db.py

    For Windows: Use Task Scheduler to run it daily at 9:00 AM.

📜 Log Output

All alerts and summary messages are logged in:

logs/monitor_log.log
