import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['fscc'], excludes = [], includes = ['re'])


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
executables = [
    Executable('wfscc.py', base=base)
]

setup(name='wfscc',
      version = '1.0.0',
      options = dict(build_exe = buildOptions),
      executables = executables)
