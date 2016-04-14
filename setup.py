from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
  name = 'dathostpython',
  packages = ['dathostpython'],
  version = '1.2',
  description = 'A python wrapper for the Dathost API',
  long_description = long_description,
  author = 'Miles Budden',
  author_email = 'miles@budden.net',
  url = 'https://github.com/pbexe/dathost-python',
  keywords = ['dathost', 'hosting', 'wrapper'],
  classifiers = [],
)
