# Dice-Roller
A python dice rolling application using standard [dice notation](https://en.wikipedia.org/wiki/Dice_notation)

## Usage
```
roll <dice code>
```

## Installation

### Archlinux

For Archlinux there is an [AUR package](https://aur.archlinux.org/packages/dice-roller-git/) available. 
You can install the PKGBUILD manually or install with the help of your favourite AUR Helper.

#### AUR Helper
*Using pacaur as an example*

```
$ pacaur -S dice-roller-git
```

#### Manual
For manual installation of AUR packages please see to the [ArchWiki](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages)

--------

### Other Linux
#### Prerequisites
* Git
* Python 3

#### Installation
```
$ git clone https://git.xirion.net/victor/dice-roller.git
$ cd dice-roller
$ sudo python setup.py install

```
