import streamlit as st
from datetime import datetime, timedelta

# --- IMPORT LOGIC ---
# This block tries to load your logic file.
# If marco_logic.py is missing or broken, it uses a temporary "backup" so the app still runs.
try:
    from marco_logic import load_data, save_data
except ImportError:
    # BACKUP FUNCTIONS (In case marco_logic.py fails)
    if "spots" not in st.session_state:
        st.session_state["spots"] = {"1": "Free", "2": "Free", "3": "Free", "4": "Free"}
   
    def load_data():
        return {"spots": st.session_state["spots"]}
       
    def save_data(data):
        st.session_state["spots"] = data["spots"]

# --- APP INTERFACE ---
st.title("🚗 Marco Parking App")
st.subheader("Real-Time Parking Tracker")

# 1. Load the data
data = load_data()
spots = data["spots"]

# 2. Create the Layout (2 Columns)
col1, col2 = st.columns(2)

# --- LEFT COLUMN: VIEW STATUS ---
with col1:
    st.info("🅿️ Parking Status")
    # Loop through all spots to show their status
    for spot_id, status in spots.items():
        if status == "Free":
            st.success(f"Spot {spot_id}: OPEN 🟢")
        else:
            st.error(f"Spot {spot_id}: {status} 🔴")

# --- RIGHT COLUMN: CONTROLS ---
with col2:
    st.warning("🛠️ Controls")
   
    # Dropdown to select a spot
    spot_options = list(spots.keys())
    selected_spot = st.selectbox("Select a Spot:", spot_options)

    # --- PARK BUTTON ---
    if st.button("PARK NOW"):
        # Calculate current time
        current_time = (datetime.now() - timedelta(hours=5)).strftime("%I:%M %p")
       
        # Update the spot status
        spots[selected_spot] = f"Taken since {current_time}"
       
        # Save the change
        save_data(data)
       
        st.success(f"Spot {selected_spot} marked as Taken at {current_time}")
        st.rerun()

    # --- LEAVE BUTTON ---
    if st.button("LEAVE Spot (Free Up)"):
        # Update the spot status
        spots[selected_spot] = "Free"
       
        # Save the change
        save_data(data)
       
        st.success(f"Spot {selected_spot} is now Free!")
        st.rerun()

 
