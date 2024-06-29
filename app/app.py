# app.py
import streamlit as st
import pandas as pd
from scripts.read_df import read_df

def main():
    st.switch_page("./pages/options.py")

if __name__ == "__main__":
    main()