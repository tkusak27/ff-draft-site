import streamlit as st
import pandas as pd
from scripts.read_df import read_df

def view_draftboard():
    df = read_df
    st.dataframe(df)