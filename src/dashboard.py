import streamlit as st
import pandas as pd
import plotly.express as px
import time
from simulator import get_meter_readings
from report_generator import generate_report

st.set_page_config(page_title="Electricity Telemetry Dashboard", layout="wide")
st.title("Electricity Telemetry Dashboard")

# Set the update interval (in seconds)
update_interval = 5

# Create a placeholder for the real-time data
placeholder = st.empty()

# Fetch the latest meter readings
readings = get_meter_readings()
df = pd.DataFrame(readings)

# Update the placeholder with new data
with placeholder.container():
    st.subheader("Real-Time Meter Readings")
    st.dataframe(df)

    st.subheader("Power Consumption Bar Chart")
    bar_fig = px.bar(df, x='meter_id', y='power', labels={'power': 'Power (W)', 'meter_id': 'Meter ID'}, title="Current Power Consumption")
    st.plotly_chart(bar_fig, use_container_width=True)

    st.subheader("Power Consumption Distribution")
    pie_fig = px.pie(df, names='meter_id', values='power', title="Power Consumption Distribution")
    st.plotly_chart(pie_fig, use_container_width=True)

    st.subheader("Generate Report")
    selected_meter = st.selectbox("Select a meter to generate report", df['meter_id'], key="report_meter_selectbox")
    if st.button("Generate Report"):
        selected_power = df[df['meter_id'] == selected_meter]['power'].values[0]
        generate_report(selected_meter, selected_power)
        st.success(f"Report for {selected_meter} generated successfully.")

# Wait for the specified interval before rerunning
time.sleep(update_interval)
st.rerun()
