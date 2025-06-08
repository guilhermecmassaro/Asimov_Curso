import streamlit as st

# Configuring the dashboard's page
st.set_page_config(
    page_title="FIFA23 - Teams",
    page_icon="⚽️",
    layout="wide"
)


# Pulling the data from Session State
df_fifa = st.session_state['fifa_data']


# Sidebar
st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")
all_clubs = df_fifa["Club"].unique()
club_box = st.sidebar.selectbox("Escolha o clube",options= all_clubs)

#Dashboard

df_filtered_by_club = df_fifa[df_fifa["Club"] == club_box]

st.image(image=df_filtered_by_club["Club Logo"].iloc[0])
st.markdown(f"## {club_box}")