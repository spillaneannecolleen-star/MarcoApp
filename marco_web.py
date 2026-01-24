import streamlit as st
import json
import os
from datetime import datetime, timedelta


# --- 1. SETUP THE DATABASE ---
DB_FILE = "marco_db.json"

def load_data():
    if not os.path.exists(DB_FILE):
        default_data = {"spots": {"1": "Free", "2": "Free", "3": "Free", "4": "Free"}}
        with open(DB_FILE, "w") as f:
            json.dump(default_data, f)
        return default_data
   
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

# --- 2. THE APP INTERFACE ---
st.title("🚗 Marco Parking App")
st.subheader("Real-Time Parking Tracker")

data = load_data()
spots = data["spots"]

col1, col2 = st.columns(2)

with col1:
    st.info("🅿️ Parking Status")
    for spot_id, status in spots.items():
        if status == "Free":
            st.success(f"Spot {spot_id}: OPEN 🟢")
        else:
            # This shows the time info now!
            st.error(f"Spot {spot_id}: {status} 🔴")

with col2:
    st.warning("🛠️ Controls")
    selected_spot = st.selectbox("Select a Spot:", ["1", "2", "3", "4"])
   
    if st.button("PARK NOW (6:10 PM)"):
       
    current_time = (datetime.now() - timedelta(hours=5)).strftime("%I:%M %p")
        # Save the status WITH the time
        spots[selected_spot] = f"Taken since {current_time}"
        save_data(data)
        st.rerun()

    if st.button("Leave Spot (Free Up)"):
        spots[selected_spot] = "Free"
        save_data(data)
        st.rerun()

 
