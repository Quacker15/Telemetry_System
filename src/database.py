import sqlite3

def initialize_database():
    conn = sqlite3.connect('data/power_telemetry.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meters (
            meter_id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
            meter_id INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            voltage REAL,
            current REAL,
            power REAL,
            FOREIGN KEY (meter_id) REFERENCES meters (meter_id)
        )
    ''')
    
    conn.commit()
    conn.close()
