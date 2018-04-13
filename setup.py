#from distutils.core import setup
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='md')
except Exception:
    long_description = open('README.md').read()

setup(
    name='Dice-Roller',
    version='1.6.2.7',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://gitlab.xirion.net/vroest/dice-roller',
    download_url = 'https://gitlab.xirion.net/vroest/dice-roller/repository/v1.6.2.7/archive.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=long_description,
    scripts=[
        'roll',
    ]
)
