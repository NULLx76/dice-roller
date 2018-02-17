from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='md')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='Dice-Roller',
    version='1.3.1',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://git.xirion.net/victor/dice-roller',
    download_url = 'https://git.xirion.net/victor/dice-roller/archive/v1.3.1.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=long_description,
    scripts=[
        'roll',
    ]
)
