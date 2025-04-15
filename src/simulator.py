import random
import time
import sqlite3
from datetime import datetime

def simulate_readings():
    conn = sqlite3.connect('data/power_telemetry.db')
    cursor = conn.cursor()
    
    while True:
        timestamp = datetime.now()
        for meter_id in range(1, 21):
            voltage = round(random.uniform(220.0, 240.0), 2)
            current = round(random.uniform(5.0, 15.0), 2)
            power = round(voltage * current / 1000, 2)
            
            cursor.execute('''
                INSERT INTO readings (meter_id, timestamp, voltage, current, power)
                VALUES (?, ?, ?, ?, ?)
            ''', (meter_id, timestamp, voltage, current, power))
        
        conn.commit()
        print(f'Readings inserted at {timestamp}')
        time.sleep(60)
