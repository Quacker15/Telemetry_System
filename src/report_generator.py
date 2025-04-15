from docx import Document
from datetime import datetime
import pandas as pd
import sqlite3

def generate_monthly_report(month, year):
    conn = sqlite3.connect('data/power_telemetry.db')
    df = pd.read_sql_query(f'''
        SELECT meter_id, timestamp, power
        FROM readings
        WHERE strftime('%m', timestamp) = '{month:02d}' AND strftime('%Y', timestamp) = '{year}'
        ORDER BY meter_id, timestamp
    ''', conn)
    conn.close()
    
    report = Document()
    report.add_heading(f'Monthly Consumption Report - {month}/{year}', 0)
    
    for meter_id in df['meter_id'].unique():
        meter_data = df[df['meter_id'] == meter_id]
        if not meter_data.empty:
            start_power = meter_data.iloc[0]['power']
            end_power = meter_data.iloc[-1]['power']
            consumption = end_power - start_power
            
            report.add_heading(f'Meter ID: {meter_id}', level=1)
            report.add_paragraph(f'Total Consumption: {consumption} kWh')
    
    report_filename = f'reports/monthly_report_{month}_{year}.docx'
    report.save(report_filename)
    
    # Convert to PDF if needed
    # Requires 'docx2pdf' and Microsoft Word on Windows
    # from docx2pdf import convert
    # convert(report_filename)
