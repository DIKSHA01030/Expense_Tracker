import sqlite3

def reset_income_table(db_name="expenses.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Drop the old income table if it exists
    cursor.execute("DROP TABLE IF EXISTS income")

    # Recreate the income table with the correct schema
    cursor.execute("""
    CREATE TABLE income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        date DATE,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Income table has been reset successfully!")

if __name__ == "__main__":
    reset_income_table()
