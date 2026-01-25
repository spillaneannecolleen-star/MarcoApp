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

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.info("🅿️ Parking Status")
    for spot_id, status in spots.items():
        if status == "Free":
            st.success(f"Spot {spot_id}: OPEN 🟢")
        else:
            # Shows the "Taken" status in red
            st.error(f"Spot {spot_id}: {status} 🔴")

with col2:
    st.warning("🛠️ Controls")
   
    # Dropdown to select a spot
    spot_options = ["1", "2", "3", "4"]
    selected_spot = st.selectbox("Select a Spot:", spot_options)

    # --- PARK BUTTON ---
    if st.button("PARK NOW"):
        # Calculate current time (adjusting for timezone if needed)
        current_time = (datetime.now() - timedelta(hours=5)).strftime("%I:%M %p")
       
        # Save the status to the dictionary
        spots[selected_spot] = f"Taken since {current_time}"
       
        # Save the data to the file (assuming you have a save function, otherwise this just updates the screen)
        # save_data(data)
       
        st.success(f"Spot {selected_spot} marked as Taken at {current_time}")
        st.rerun()

    # --- LEAVE BUTTON ---
    if st.button("LEAVE Spot (Free Up)"):
        spots[selected_spot] = "Free"
       
        # save_data(data) # Uncomment this if you have the save function ready
       
        st.success(f"Spot {selected_spot} is now Free!")
        st.rerun()

 

            
        

    

 
