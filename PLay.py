from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(name = 'NameOfModule',
      version = '1.0',
      url = 'http://www.coret.cn',
      py_modules = 'NameOfModule'
)

