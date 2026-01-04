import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "attrition.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            monthly_income INTEGER,
            job_satisfaction INTEGER,
            work_life_balance INTEGER,
            total_working_years INTEGER,
            years_at_company INTEGER,
            years_with_manager INTEGER,
            risk_score REAL,
            prediction TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
