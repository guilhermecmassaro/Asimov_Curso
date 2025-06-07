import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta

# ----------------------------------------- DATABASES - SESSION STATES ----------------------------------------------

# Important session states
if "fifa_data" not in st.session_state:
    df_fifa = pd.read_csv(r'datasets\CLEAN_FIFA23_official_data.csv',index_col=0)
    df_fifa = df_fifa[df_fifa["Contract Valid Until"] >= datetime.today().year]
    df_fifa = df_fifa[df_fifa["Value(£)"] > 0]
    df_fifa = df_fifa.sort_values(by="Overall",ascending=False)
    st.session_state["fifa_data"] = df_fifa


# ----------------------------------------- PAGES ----------------------------------------------

# Define the pages
main_page = st.Page(r"pages\1_🏡_Home.py")
page_2 = st.Page(r"pages\2_⛹️‍♂️_Players.py")
page_3 = st.Page(r"pages\3_⚽_Teams.py")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()