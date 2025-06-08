import streamlit as st

# Configuring the dashboard's page
st.set_page_config(
    page_title="FIFA23 - Players",
    page_icon="⛹️‍♂️",
    layout="wide"
)

# Pulling the data from Session State
df_fifa = st.session_state['fifa_data']

# Sidebar

all_clubs = df_fifa["Club"].unique()
club_box = st.sidebar.selectbox("Escolha o clube",options= all_clubs)

club_players = df_fifa[df_fifa["Club"] == club_box]['Name']
players_box = st.sidebar.selectbox("Escolha o jogador",options= club_players)

st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")


# Dashboard
df_line_player = df_fifa[df_fifa['Name'] == players_box].iloc[0] # Iloc retorna a string, sem isso dá erro ao selecionar o dataframe

st.image(df_line_player["Photo"])
st.title(df_line_player['Name'])

st.markdown(f"Clube: {df_line_player['Club']}")
st.markdown(f"Posição: {df_line_player['Position']}")

# --
col1, col2, col3 = st.columns(3)

with col1: 
    st.markdown(f"**Idade:** {df_line_player['Age']}")

with col2: 
    st.markdown(f"**Altura:** {df_line_player['Height(cm.)']/100}")

with col3: 
    st.markdown(f"**Peso:** {df_line_player['Weight(lbs.)']*0.453:.1f}")

# --

st.divider()

# --
st.subheader(f"Overall {df_line_player['Overall']}")
st.progress(value=int(df_line_player[['Overall']]))
# --

# --

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label = "Valor de mercado", value=f"£ {df_line_player['Value(£)']:,}")

with col2:
    st.metric(label = "Remuneração Semanal", value=f"£ {df_line_player['Wage(£)']:,}")

with col3:
    st.metric(label = "Cláusula de rescisão", value=f"£ {df_line_player['Release Clause(£)']:,}")
 


# --

