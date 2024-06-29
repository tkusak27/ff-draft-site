import streamlit as st

# Draftboard on top half
with st.container(border=True):
    st.subheader("Draftboard")
    #st.markdown(f"{st.session_state['scoring_setting']}, {st.session_state['num_teams']} teams, pick #{st.session_state['draft_position']}")
    with st.container(border=True):
        st.text("ok")

bottom_cols = st.columns([1, 1])
# Current team in bottom left quadrant
with bottom_cols[0]:
    with st.container(border=True):
        st.subheader("Current Team")

# Suggested pick in bottom right quadrant
with bottom_cols[1]:
    with st.container(border=True):
        st.subheader("Suggested pick")
