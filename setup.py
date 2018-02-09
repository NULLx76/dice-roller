from distutils.core import setup

setup(
    name='Dice-Roller',
    version='0.4',
  	license='GPL3',
    long_description=open('README.md').read(),
    scripts = [
            'roll',
        ]
)

