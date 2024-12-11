import sys
import os
import cx_Freeze
from cx_Freeze import setup, Executable

# Aumentar a profundidade máxima de recursão
sys.setrecursionlimit(5000)

# Definir o que deve ser incluído na pasta final
arquivos = ['table.ico']

# Configurar a saída dos arquivos
config = Executable(
    script='App.py',
    icon='table.ico'
)

# Detalhes
setup(
    name='Tabelas Db',
    version='0.1',
    description='Exibir tabelas do banco de dados',
    author='Cauan Neves',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
