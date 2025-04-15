import streamlit as st
import pandas as pd
import sqlite3

def real_time_dashboard():
    conn = sqlite3.connect('data/power_telemetry.db')
    df = pd.read_sql_query('''
        SELECT meter_id, timestamp, voltage, current, power
        FROM readings
        ORDER BY timestamp DESC
        LIMIT 50
    ''', conn)
    conn.close()
    
    st.title("Real-Time Power Meter Readings")
    st.dataframe(df)
