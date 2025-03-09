import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo", 
    "Australia/Sydney", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata"
]

# App title with styling
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🕒 Time Zone Converter</h1>
    <p style='text-align: center; font-size: 18px;'>Easily convert and compare time zones</p>
    <hr>
""", unsafe_allow_html=True)

# Multi-select widget for time zone selection
selected_timezones = st.multiselect(
    "🌍 Select Timezones:", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display selected time zones
st.subheader("📅 Current Time in Selected Timezones")

for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.markdown(f"<p style='font-size:18px;'><b>{tz}:</b> {current_time}</p>", unsafe_allow_html=True)

# Time conversion section
st.subheader("🔄 Convert Time Between Timezones")

# User input for time conversion
current_time = st.time_input("⏰ Select Time:", value=datetime.now().time())
from_tz = st.selectbox("📍 From Timezone:", TIME_ZONES, index=0)
to_tz = st.selectbox("🌏 To Timezone:", TIME_ZONES, index=1)

# Convert time button
if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: {converted_time}")

# Footer styling
st.markdown("""
    <hr>
    <p style='text-align: center;'>Made with ❤️ Bisma Yousuf</p>
""", unsafe_allow_html=True)
