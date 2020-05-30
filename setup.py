#!/usr/bin/env python

import re

from setuptools import setup, find_packages

cmdclass = {}

with open('app/__init__.py') as f:
    _version = re.search(r'__version__\s+=\s+\"(.*)\"', f.read()).group(1)

setup(name='OnePage',
      version=_version,
      packages=find_packages(),
      description='Simple ScratchPad',
      author='Namuan',
      author_email='info@deskriders.dev',
      license='MIT',
      url='https://deskriders.dev',
      entry_points={
          'gui_scripts': ['app=app.__main__:__main__.py'],
      },
      cmdclass=cmdclass)
