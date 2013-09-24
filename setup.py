import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['fscc'], excludes = [], includes = ['re'])
    
executables = [
    Executable('wfscc.py')
]

setup(name='wfscc',
      version = '1.0.0',
      options = dict(build_exe = buildOptions),
      executables = executables)
