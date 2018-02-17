from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='md')
except Exception:
    long_description = open('README.md').read()

setup(
    name='Dice-Roller',
    version='1.5',
    license='GPL3',
    author = 'Victor Roest',
    author_email = 'victor@xirion.net',
    url = 'https://git.xirion.net/victor/dice-roller',
    download_url = 'https://git.xirion.net/victor/dice-roller/archive/v1.5.tar.gz',
    keywords = ['dnd', 'dice'],
    description= 'A dice-rolling application using standard dice notation',
    long_description=long_description,
    scripts=[
        'roll',
    ]
)
