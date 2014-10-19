#!/usr/bin/env python

import codecs
import os
from setuptools import setup, find_packages



PACKAGE = 'pyopendata'
README = 'README.rst'
REQUIREMENTS = 'requirements.txt'
# required modules for test and doc build
REQUIREMENTS_TEST = 'requirements_test.txt'

VERSION = '0.0.3.dev'

def read(fname):
  # file must be read as utf-8 in py3 to avoid to be bytes
  return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

def write_version_py(filename=None):
    cnt = """\
version = '%s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % VERSION)
    finally:
        a.close()

version_file = os.path.join(os.path.dirname(__file__), 'pyopendata', 'version.py')
write_version_py(filename=version_file)

setup(name=PACKAGE,
      version=VERSION,
      description='Python utility to get open data from some popular websites',
      long_description=read(README),
      author='sinhrks',
      author_email='sinhrks@gmail.com',
      url='http://pyopendata.readthedocs.org',
      license = 'BSD',
      packages=find_packages(),
      package_data={'pyopendata.io': ['tests/data/jsdmx/*.json',
                                      'tests/data/jstat/*.json',
                                      'tests/data/sdmx/*.json']},
      install_requires=list(read(REQUIREMENTS).splitlines()))

