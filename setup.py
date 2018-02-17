from distutils.core import setup

setup(
    name='Dice-Roller',
    version='1.2',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://git.xirion.net/victor/dice-roller',
    download_url = 'https://git.xirion.net/victor/dice-roller/archive/v1.2.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=open('README.md').read(),
    scripts=[
        'roll',
    ]
)
