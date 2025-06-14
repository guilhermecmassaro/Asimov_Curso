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
# st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")
all_clubs = df_fifa["Club"].unique()
club_box = st.sidebar.selectbox("Escolha o clube",options= all_clubs)

#Dashboard

df_filtered_by_club = df_fifa[df_fifa["Club"] == club_box].set_index("Name")

st.image(image=df_filtered_by_club["Club Logo"].iloc[0])
st.markdown(f"## {club_box}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered_by_club[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     label = "Overall",format="%d", min_value=0, max_value=100 # formatação de inteiro
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     label = "Weekly Wage",format="£%f", min_value=0, max_value=df_filtered_by_club['Wage(£)'].max() # formatação de inteiro
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
                                  
            
                 



             })