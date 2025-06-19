import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
from pathlib import Path

# ----------------------------------------- DATABASES - SESSION STATES ----------------------------------------------

# Important session states
if "vendas" not in st.session_state:
    df_vendas = pd.read_csv("datasets/vendas.csv", sep = ";", decimal=",", index_col=0, parse_dates=True)
    st.session_state["vendas"] = df_vendas

if "produtos" not in st.session_state:
    df_produtos = pd.read_csv("datasets/produtos.csv", sep = ";", decimal=",", index_col=0, parse_dates=True)
    st.session_state["produtos"] = df_produtos

if "filiais" not in st.session_state:
    df_filiais = pd.read_csv("datasets/filiais.csv", sep = ";", decimal=",", index_col=0, parse_dates=True)
    st.session_state["filiais"] = df_filiais


# ----------------------------------------- PAGES ----------------------------------------------

# Define the pages
main_page = st.Page("pages/1_Home.py")
page_2 = st.Page("pages/2_Visão_Geral.py")
page_3 = st.Page("pages/3_Visualização_Dinâmica.py")
page_4 = st.Page("pages/4_Tabelas.py")
page_5 = st.Page("pages/5_Adição_e_Remoção_de_Vendas.py")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()