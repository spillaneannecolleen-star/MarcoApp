import streamlit as st
from streamlit_folium import st_folium
import folium
from marco_logic import SpotProvider, SpotSeeker, UserSystem

if 'user_sys' not in st.session_state:
    st.session_state.user_sys = UserSystem()
if 'seeker' not in st.session_state:
    st.session_state.seeker = SpotSeeker()

st.set_page_config(page_title="Marco", page_icon="🚗")

st.title("🚗 Marco")

tab1, tab2, tab3 = st.tabs(["Leave", "Find", "Leaderboard"])

with tab2:
    st.header("Available Spots")
   
    # Map (kept simple for this version)
    m = folium.Map(location=[28.5383, -81.3792], zoom_start=16)
    results = st.session_state.seeker.search_spots("")
    for s in results:
        folium.Marker([s['lat'], s['lon']], popup=s['name']).add_to(m)
    st_folium(m, width=700, height=300)

    st.divider()

    # List of spots with "Report False" buttons
    for i, spot in enumerate(results):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"✅ **{spot['name']}** (Posted by {spot['posted_by']})")
        with col2:
            # Unique key for every button
            if st.button("🚩 False", key=f"report_{i}"):
                note = st.session_state.user_sys.report_false_spot(spot['posted_by'])
                st.toast(note)
                st.warning("Thank you for keeping Marco accurate!")

with tab3:
    st.header("Top Scouts")
    # Using a Dataframe for a more professional "App Store" table look
    st.dataframe(st.session_state.user_sys.get_leaderboard(), use_container_width=True, hide_index=True)

 
