import streamlit as st
from scripts.read_df import read_df
from utils.draftboard import Draftboard


# Draftboard on top half
with st.container(border=True):
    draftboard = Draftboard()
    draftboard.render_draftboard()        
    

bottom_cols = st.columns([1, 1])
# Current team in bottom left quadrant
with bottom_cols[0]:
    with st.container(border=True):
        st.subheader("Current Team")
        st.dataframe(st.session_state["roster"])

# Suggested pick in bottom right quadrant
with bottom_cols[1]:
    with st.container(border=True):
        st.subheader("Suggested pick")
