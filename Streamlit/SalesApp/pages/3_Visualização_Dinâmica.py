import streamlit as st

# Configuring the dashboard's page
st.set_page_config(
    page_title="Page3",
    page_icon="⚽️",
    layout="wide"
)

# Pulling the data from Session State
df_vendas = st.session_state["vendas"]
df_produtos = st.session_state["produtos"]
df_filiais = st.session_state["filiais"]