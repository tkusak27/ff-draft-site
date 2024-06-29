import streamlit as st

with st.columns([1,4,1])[1]:
    with st.container(border=True):
        st.markdown('<h2 style="text-align: center;">Configure Dynasty Draft Settings</h2>', unsafe_allow_html=True)

        scoring_setting = st.selectbox("Select scoring format:", ["Standard", "Half-PPR", "PPR"])
        num_teams = st.number_input("Enter the amount of teams:", min_value=4, max_value=16, step=2)
        draft_position = st.number_input(f"Enter your draft position:", min_value=1, max_value=num_teams, step=1)

        st.warning("Currently this application only supports default superflex settings (1QB, 2RB, 3WR, 1TE, 1FLX, 1SFLX)")
        submit_button = st.button("Draft")

        if submit_button:
            # update session state values
            st.session_state["scoring_setting"] = scoring_setting
            st.session_state["num_teams"] = num_teams
            st.session_state["draft_position"] = draft_position

            st.switch_page("pages/draft.py")