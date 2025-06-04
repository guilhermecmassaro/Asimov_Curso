import pandas as pd
import streamlit as st
import time

# ----------------------------------------------------- PAGE LAYOUT --------------------------------------------------------------------------
st.set_page_config(layout="wide",page_title="Spotify Streamlit App")


# ----------------------------------------------------- DATA PULL --------------------------------------------------------------------------

# Cria uma fórmula que guarda o dado em cache
@st.cache_data
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    time.sleep(5) # simula um carregamento pesado para entender o cache
    return df

# Inicializa o session state (de acordo com a documentação oficial)
df = load_data(csv_file='01 Spotify.csv')
if "df_spotify" not in st.session_state:
    st.session_state["df_spotify"] = df # Guardando os dados em um state para ser acessado mais facilmente por outros states/pessoas

df.set_index("Title", inplace=True)


# ----------------------------------------------------- DASHBOARD --------------------------------------------------------------------------

# Filter Artist
artists = df["Artist"].unique()
artist_box = st.sidebar.selectbox(label = "Artista", options = artists) # Se você adicionar um "sidebar" apenas depois do st, ele vai ficar na lateral
filtro = ((df["Artist"] == artist_box))
df_filtered_by_artist = df[filtro]

# Filter Album
albums = df_filtered_by_artist["Album"].unique()
album_box = st.selectbox(label = "Album", options = albums)
df_filtered_by_album = df[df["Album"] == album_box]


# Gráficos

col1, col2 = st.columns(2) # Se adicionarmos um iterável como st.columns([0.7,0.3]), isso diria para a biblioteca que gostaria de 70% do espaço para um e 30% para outro

col1.bar_chart(data = df_filtered_by_album["Stream"])

col2.line_chart(data = df_filtered_by_album["Danceability"])
 
