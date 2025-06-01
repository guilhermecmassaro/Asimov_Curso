import pandas as pd
import streamlit as st

# Page layout
st.set_page_config(layout="wide",page_title="Spotify Streamlit App")



# Dataframe
df = pd.read_csv('01 Spotify.csv')
df.set_index("Title", inplace=True)

# Filter Artist
artists = df["Artist"].unique()
artist_box = st.selectbox(label = "Artista", options = artists)
filtro = ((df["Artist"] == artist_box))
df_filtered_by_artist = df[filtro]

# Filter Album
albums = df_filtered_by_artist["Album"].unique()
album_box = st.selectbox(label = "Album", options = albums)


# Gráfico de linha
display = st.checkbox('Display chart')
if display:
    st.bar_chart(data = df[df["Album"] == album_box]["Stream"], horizontal=True)
 
