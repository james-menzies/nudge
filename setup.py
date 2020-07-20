from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'include_files': ['src/resources/']}

base = 'Console'

executables = [
    Executable('src/main.py', base=base, targetName='StringRoster')
]

setup(name='String Roster',
      version = '1.0',
      description = 'Utilityyyyy',
      options = {'build_exe': build_options},
      executables = executables)
