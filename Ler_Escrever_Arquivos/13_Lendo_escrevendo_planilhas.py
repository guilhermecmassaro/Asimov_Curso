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



# Adicionando coluna de index




# Lendo colunas específicas
