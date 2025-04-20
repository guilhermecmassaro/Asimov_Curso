from pathlib import Path
import os
import shutil

# mkdir = make diretory
# exist_ok = Se caso a pasta já existir, não faz nada, garantindo que não de erro
# parents = True  Cria mais de uma pasta ao mesmo tempo (destino subsequentes)
# rmdir() = remove diretory


# Criando pasta
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'

caminho_pasta_destino.mkdir(exist_ok=True)  # mkdir = make directory
'''

# Criando pasta com todos as pastas anteriores necessárias
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino51'

caminho_pasta_destino.mkdir(parents=True,exist_ok=True)
'''

# Copiando pastas
'''
pasta_atual = Path(__file__).parent
shutil.copytree(src = pasta_atual / 'destino5', dst= pasta_atual / 'destino1' / 'destino5')
'''

# Deletando pastas vazias
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino5' / 'destino51'
if pasta_remover.exists():
    pasta_remover.rmdir() # Só deleta pastas VAZIAS
'''
    
# Deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1'
if pasta_remover.exists():
    shutil.rmtree(pasta_remover) # Deleta pastas COM CONTEÚDO

caminho_pasta_destino = pasta_atual / 'destino1'/'destino5' / 'destino51'
caminho_pasta_destino.mkdir(parents=True,exist_ok=True)




