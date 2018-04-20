#from distutils.core import setup
from setuptools import setup


long_description = open('README.rst').read()

setup(
    name='Dice-Roller',
    version='1.7.1',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://gitlab.xirion.net/vroest/dice-roller',
    download_url = 'https://gitlab.xirion.net/vroest/dice-roller/repository/v1.7.1/archive.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=long_description,
    scripts=[
        'roll',
    ]
)
