#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import chardet
from setuptools import setup, find_packages


README = ''
try:
    f = open('README.rst')
    README = f.read()
    f.close()
except:
    pass

setup(name='chardet2',
      version=chardet.__version__,
      author='Mark Pilgrim',
      author_email='mark@diveintomark.com',
      packages=find_packages(),
      description = "Character encoding auto-detection in Python 3",
      long_description=README,
      license="LGPL",
      platforms=["Independent"],
      url="https://github.com/byroot/chardet",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Text Processing :: Linguistic",
      ],
      scripts=['bin/chardet2']
)
