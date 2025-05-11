import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).parent

# Lendo tabelas com Dataframe
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx') # Lê a primeira aba
print(tabela_clientes.head())
'''

# Lendo aba específica
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC') # Lê a aba escolhida
print(tabela_clientes.head())
'''


# Modificando header
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', header = 0) 
print(tabela_clientes.head())
'''

# Adicionando coluna de index
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', index_col = 0) 
print(tabela_clientes.head())

'''

# Lendo colunas específicas
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', usecols= 'A:B') 
# tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', usecols= [0,1])
print(tabela_clientes.head())
'''

# Comentários sobre decimals e thousands
# Para Decimal
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', decimal = '.') 
print(tabela_clientes.head())

# Para Thousands
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name = 'SC', thousands = '.') 
print(tabela_clientes.head())
'''

# Escrevendo na planilha

# Nesse formato, ele cria uma cópia apenas com a aba principal ou que você selecionou
'''
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')
tabela_clientes.to_excel(pasta_atual / 'clientes_copia.xlsx')
'''

# Escrevendo diversas abas
tabela_clientes_rs = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RS') # Dataframe 1
tabela_clientes_sc = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC') # Dataframe 2

with pd.ExcelWriter(path= pasta_atual / 'clientes_copia.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(excel_writer= nova_planilha, sheet_name= 'RS', index=False)
    tabela_clientes_sc.to_excel(excel_writer= nova_planilha, sheet_name= 'SC', index=False)