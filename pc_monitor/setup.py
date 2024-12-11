import sys
import os
import cx_Freeze
from cx_Freeze import setup, Executable

# Aumentar a profundidade máxima de recursão
sys.setrecursionlimit(5000)

# Definir o que deve ser incluído na pasta final
arquivos = ['pc.ico']

# Configurar a saída dos arquivos
config = Executable(
    script='App.py',
    icon='pc.ico'
)

# Detalhes
setup(
    name='Chamado Pc/Monitor',
    version='0.1',
    description='Um aplicativo feito para melhorar a eficiência na abertura de chamado. Esta versão não é a final, o app pode conter bugs e ser incapaz de lidar com problemas causados pelo usuário.',
    author='Cauan Neves',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
