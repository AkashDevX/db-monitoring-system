import psycopg2
from datetime import datetime

# Database connection config
DB_NAME = "monitor_db"
DB_USER = "postgres"      # change if needed
DB_PASSWORD = "123"          # add password if needed
DB_HOST = "localhost"
DB_PORT = "5432"

# Alert thresholds
SALES_THRESHOLD = 10000
ROW_COUNT_THRESHOLD = 10000  # example threshold for row count

# Log file path
LOG_FILE = "../logs/monitor_log.log"


def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")
    print(message)


def main():
    try:
        # Connect to DB
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor()

        # 1. Simple health check
        cursor.execute("SELECT 1;")
        health = cursor.fetchone()
        if health and health[0] == 1:
            log_message("DB Health Check: Connection OK.")
        else:
            log_message("DB Health Check: Unexpected response.")

        # 2. Total row count in sales_data
        cursor.execute("SELECT COUNT(*) FROM sales_data;")
        row_count = cursor.fetchone()[0]
        log_message(f"Total rows in sales_data: {row_count}")
        if row_count > ROW_COUNT_THRESHOLD:
            log_message(f"ALERT: Row count exceeds threshold! ({row_count} rows)")

        # 3. High sales quantity alert
        cursor.execute("""
            SELECT product_name, quantity_sold FROM sales_data
            WHERE quantity_sold > %s
        """, (SALES_THRESHOLD,))
        results = cursor.fetchall()
        if results:
            for product, qty in results:
                alert_msg = f"ALERT: High sales quantity for '{product}' - {qty} units sold."
                log_message(alert_msg)
        else:
            log_message("All sales quantities are within normal limits.")

        # 4. Daily sales summary
        cursor.execute("SELECT SUM(quantity_sold) FROM sales_data;")
        total_sales = cursor.fetchone()[0]
        log_message(f"Daily sales summary: Total quantity sold = {total_sales}")

        cursor.close()
        conn.close()

    except Exception as e:
        log_message(f"ERROR: {e}")


if __name__ == "__main__":
    main()
