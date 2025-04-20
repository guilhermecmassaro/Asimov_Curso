from pathlib import Path
import shutil # Criando em cima do módulo 'os', mas ele permite certas praticidades para o usuário
import os

# Copiando arquivo com copyfile
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(src = caminho_arquivo, dst= caminho_arquivo_destino)
'''

# Copiando arquivo com copy
# Substitui o metadados, é o modelo que o cara usa
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2' 

shutil.copy(src = caminho_arquivo, dst= caminho_pasta_destino)
'''

# Copiando arquivo com copy2 
# (a diferença é que neste método também é copiado os metadados deste arquivo)
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3' 

shutil.copy(src = caminho_arquivo, dst= caminho_pasta_destino)
'''

# Movendo arquivos
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino1' 

shutil.move(src = caminho_arquivo, dst= caminho_pasta_destino)
'''

# Deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual /'destino3' /'texto.txt'

# shutil.copyfile(src = caminho_arquivo, dst= caminho_arquivo_destino)
if caminho_arquivo.exists():
    os.remove(caminho_arquivo)
