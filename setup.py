#from distutils.core import setup
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='md')
except Exception:
    long_description = open('README.md').read()

setup(
    name='Dice-Roller',
    version='1.6.1',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://git.xirion.net/vroest/dice-roller',
    download_url = 'https://git.xirion.net/vroest/dice-roller/archive/v1.6.1.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=long_description,
    scripts=[
        'roll',
    ]
)
