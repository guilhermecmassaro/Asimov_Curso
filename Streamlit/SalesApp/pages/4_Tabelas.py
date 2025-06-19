import streamlit as st

# Configuring the dashboard's page
st.set_page_config(
    page_title="Tabelas",
    page_icon="📋",
    layout="wide"
)

# Pulling the data from Session State
df_vendas = st.session_state["vendas"]
df_produtos = st.session_state["produtos"]
df_filiais = st.session_state["filiais"]

# SideBar

st.sidebar.markdown("# Seleção de Tabelas")
table = st.sidebar.selectbox(label="Selecione a tabela que deseja ver",options=['Vendas','Produtos','Filiais'])

# Dashboard/ Sidebar

if table == 'Vendas':

    # Adding the specific Vendas filters
    st.sidebar.divider()
    st.sidebar.markdown('# Filtrar a tabela')
    vendas_columns = st.sidebar.multiselect(label='Selecione as colunas da tabela',options= df_vendas.columns, default=df_vendas.columns)
    
    # Filtering the Vendas Dataframe by the specific filters
    df_vendas_filtered = df_vendas[vendas_columns]

     # Creating the buttons
    st.sidebar.divider()
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        vendas_column_to_be_filtered = st.selectbox(label="Filtrar coluna",options=vendas_columns)
        vendas_column_to_be_filtered_btn = st.button(label="Filtrar")
    with right_column:
        vendas_value_to_be_filtered = st.selectbox(label="Valor do Filtro",options=df_vendas[vendas_column_to_be_filtered].unique())
        clean_btn = st.button(label="Limpar")
    
    # Creating the funcionality from buttons
    if vendas_column_to_be_filtered_btn:
        # Filter a specific value from a specific column
        df_vendas_filtered = df_vendas_filtered[df_vendas_filtered[vendas_column_to_be_filtered] == vendas_value_to_be_filtered]
   
    if clean_btn:
        # Return all data but keeps the initial columns from the Dataframe
        df_vendas_filtered = df_vendas_filtered

else:
    df_vendas_filtered = df_vendas

# Dashboard

# Create dictionary to map the filter's parameter and the respective table to make the code cleaner
dict_table_to_display = {
    'Produtos' : df_produtos,
    'Filiais': df_filiais,
    'Vendas':df_vendas_filtered,
}

# Display the dataframe in the dashboard
st.dataframe(data=dict_table_to_display[table])