import os
from pathlib import Path

# os.path.getsize()

# Desenvolver um script que retorna o tamanho dos arquivos das pastas

# ------------------------------- MINHA RESOLUÇÃO ----------------------------
'''
def retorna_tamanho_dos_diretorios(dir_path, profundidade = None):
    dir_path = Path(dir_path)
    arquivos = dir_path.glob('**/*')
    for arquivo in arquivos:
        if arquivo.is_file():
            print(f'--{arquivo.stem} {os.path.getsize(arquivo)} mb')
        else:
            print(f'{arquivo.stem} {os.path.getsize(arquivo)} mb')
    
    return

retorna_tamanho_dos_diretorios(dir_path=Path.home())
'''


# ---------------------- SOLUÇÃO DO PROFESSOR ---------------------------------

from pathlib import Path
import os


def retorna_tamanho_arquivos(caminho, profundidade = 1, tamanho_linha = 0):
    for diretorio in caminho.glob('*'):
        if diretorio.is_dir() and not diretorio.name.startswith('.'):
            tamanho_diretorio = 0
            for arquivo in diretorio.glob('**/*'):
                if arquivo.is_file():
                    tamanho_diretorio =+ os.path.getsize(arquivo)
            print('--' * tamanho_linha,diretorio.name, round(tamanho_diretorio/1024/1024,3),'mb')
            if profundidade > 1:
                retorna_tamanho_arquivos(diretorio, profundidade -1, tamanho_linha + 1)

caminho = Path.home()  / 'Documents'
# caminho = Path('D:/')
# retorna_tamanho_arquivos(caminho=caminho, profundidade=1)
print(caminho.name)
