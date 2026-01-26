import streamlit as st
from datetime import datetime, timedelta

# --- PAGE SETUP (Make it Orange-themed) ---
st.set_page_config(page_title="Marco", page_icon="🍊", layout="centered")

# Custom CSS to make the Title Orange
st.markdown("""
    <style>
    h1 {
        color: #FF8800; /* Bright Orange */
    }
    div.stButton > button:first-child {
        border-color: #FF8800;
        color: #FF8800;
    }
    </style>
    """, unsafe_allow_html=True)

# --- IMPORT LOGIC ---
try:
    from marco_logic import load_data, save_data, reset_db
except ImportError:
    st.error("Logic file not found!")

st.title("🍊 Marco Parking App")
st.subheader("Real-Time Parking Tracker")

# 1. Load Data
data = load_data()
spots = data["spots"]

col1, col2 = st.columns(2)

# --- LEFT COLUMN: STATUS ---
with col1:
    st.info("🅿️ Parking Status")
    for spot_id, status in spots.items():
        if status == "Free":
            st.success(f"{spot_id}: OPEN 🟢")
        else:
            # st.warning shows up as Orange/Yellow!
            st.warning(f"{spot_id}: {status} 🟠")

# --- RIGHT COLUMN: CONTROLS ---
with col2:
    st.write("🛠️ **Controls**")
   
    # Dropdown to select a spot
    spot_options = list(spots.keys())
    selected_spot = st.selectbox("Select a Spot:", spot_options)

    # PARK BUTTON
    if st.button("PARK NOW"):
        current_time = (datetime.now() - timedelta(hours=5)).strftime("%I:%M %p")
        spots[selected_spot] = f"Taken since {current_time}"
        save_data(data)
        st.rerun()

    # LEAVE BUTTON
    if st.button("LEAVE Spot"):
        spots[selected_spot] = "Free"
        save_data(data)
        st.success(f"{selected_spot} is Free!")
        st.rerun()

    st.markdown("---")
    # RESET BUTTON (Use this once to get the new spot names!)
    if st.button("⚠️ RESET ALL SPOTS"):
        data = reset_db()
        st.rerun()

 
