from setuptools import setup, find_packages
from codecs import open
from os import path

current_directory = path.abspath(path.dirname(__file__))

def read_long_description():
  with open(path.join(current_directory, 'README.md'), encoding='utf-8') as input:
    return input.read()

setup(
  name='gitvtag',
  version= '0.1',

  description='A git subcommand for simple and straightforward version tagging',
  long_description=read_long_description(),
  url='https://github.com/SashaOv/git-vtag',

  author= 'Sasha Ovsankin',
  author_email= 'sasha@ovsankin.com',
  license= 'Apache License, Version 2.0',
  packages= find_packages(),
  package_data={ '': ['README.md', 'LICENSE'] },
  install_requires= [ ],
  entry_points={
    'console_scripts': [
      'git-vtag = gitvtag.cli:cli'
    ],
  }
)

