import sys
import os
import cx_Freeze
from cx_Freeze import setup, Executable

# Aumentar a profundidade máxima de recursão
sys.setrecursionlimit(5000)

# Definir o que deve ser incluído na pasta final
arquivos = ['printer.ico']

# Configurar a saída dos arquivos
config = Executable(
    script='App.py',
    icon='printer.ico'
)

# Detalhes
setup(
    name='Solicitação de Toner',
    version='2.0',
    description='Um aplicativo feito para melhorar a eficiência na  solicitação de toner.',
    author='Cauan Neves',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
