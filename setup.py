from cx_Freeze import setup, Executable
from pathlib import Path

install_path = Path.home().joinpath("StringUtility")

build_options = {'packages': [],
                 'excludes': [],
                 'include_files': ['src/resources/'],
                 'build_exe': install_path}

base = 'Console'

executables = [
    Executable('src/main.py', base=base, targetName='StringRoster',
               shortcutDir="DesktopFolder", shortcutName="String Roster")
]

setup(name='String Roster',
      version='1.0',
      description='Utilityyyyy',
      options={'build_exe': build_options},
      executables=executables)
