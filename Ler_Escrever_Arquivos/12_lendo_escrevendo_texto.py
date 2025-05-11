from pathlib import Path

# Relembrando alguns tópicos
"""

from pathlib import Path

caminho = Path(__file__).parent

for files in caminho.glob('*'):
    print(files)

"""

# ------------------ Retornando para a aula -----------------------------

# Lendo um arquivo forma não recomendada

"""
pasta_atual = Path(__file__).parent

lista_compras = open(pasta_atual / 'lista_de_compras.txt') # Open o python criar um objeto de arquivo, como se ele tivesse apertado duas vezes

print(lista_compras.read())

lista_compras.close()
# Não é recomendado pois se tivermos fazendo isso com muitas arquivos, podemos esquecer de fechá-los
"""

# Lendo arquivo forma recomendada
'''
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras: # Não precisa dar close()
    print(lista_compras.read())
'''


# Lendo linha a linha
'''
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end='') # Esse end retira o espaço que estava ficando no print
        linha = lista_compras.readline()
'''

# Lendo todas as linhas
'''
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    lista = lista_compras.readlines()
    # Eu criei o que está abaixo
    for word in lista:
        print(word, end = '')
'''


# Escrevendo arquivos
'''
itens_ja_compras = ['farinha','fermento','agua']
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode = 'w') as lista_atualizada:
    for item in itens_lista:
        item = item.strip()
        if not item in itens_ja_compras:
            lista_atualizada.write(item + '\n')
'''

# Escrevendo linha a linha
'''
itens_ja_compras = ['farinha','fermento','agua']
pasta_atual = Path(__file__).parent

# - Le a lista atual de compras
with open(pasta_atual / 'lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

# - Cria uma nova lista vazia para os itens faltantes
itens_lista_atualizada = []
# - Itera sobre os itens da lista de compras
for item in itens_lista:
    # - Se o item não estiver na lista de compras ja feitas
    if not item.replace('\n','') in itens_ja_compras:
        itens_lista_atualizada.append(item)

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    lista_atualizada.writelines(itens_lista_atualizada)
'''

# Acrescentando valores a um arquivo
pasta_atual = Path(__file__).parent

novos_itens = ['banana']
with open(pasta_atual / 'lista_de_compras.txt', mode= 'a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens) # Como estamos mexendo com uma lista, devemos utilizar o writelines