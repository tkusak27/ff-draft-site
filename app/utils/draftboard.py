import streamlit as st
import pandas as pd

class Draftboard:

    def __init__(self):
        self.view = st.empty()

    def render_draftboard(self):
        with self.view:
            with st.container(border=True):
                st.subheader("Draftboard")
                selection = st.dataframe(st.session_state["draftboard"],hide_index=True, selection_mode="single-row", on_select="rerun")

                if selection['selection']['rows']:
                    row = selection['selection']['rows'][0]
                    player_name = st.session_state['draftboard']['PLAYER NAME'][row]
                    
                    cols = st.columns([1,3,1,3,1])
                    with cols[1]:
                        draft_player = st.button(f"Draft {st.session_state['draftboard']['PLAYER NAME'][row]}?")
                    with cols[3]:
                        remove_player = st.button(f"Remove {st.session_state['draftboard']['PLAYER NAME'][row]}?")
                    
                    if draft_player:
                        # delete player from dataframe
                        # add player to roster
                        st.session_state["draftboard"] = st.session_state["draftboard"].drop(row).reset_index(drop=True)
                        self.render_draftboard()

                    if remove_player:
                        st.session_state["draftboard"] = st.session_state["draftboard"].drop(row).reset_index(drop=True)
                        self.render_draftboard()

    # Draftboard on top half
with st.container(border=True):
    st.subheader("Draftboard")
    selection = st.dataframe(st.session_state["draftboard"],hide_index=True, selection_mode="single-row", on_select="rerun")
    if selection['selection']['rows']:
        row = selection['selection']['rows'][0]
        player_name = st.session_state['draftboard']['PLAYER NAME'][row]
        
        button = st.button(f"Draft {st.session_state['draftboard']['PLAYER NAME'][row]}?")
        
        if button:
            # delete player from dataframe
            # add player to roster
            st.session_state["draftboard"] = st.session_state["draftboard"].drop(row).reset_index(drop=True)
            st.experimental_rerun()
            