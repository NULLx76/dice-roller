Deprecation Notice
===========
`Roll-rs <https://github.com/finitum/roll-rs>`_ has superseded this project and thus this project will not receive any updates.
Any features requests are kindly to be redirected to the aforementioned roll-rs.

Dice-Roller
-----

A python dice rolling application using standard `dice
notation <https://en.wikipedia.org/wiki/Dice_notation>`__

Usage
-----

::

    roll <dice code>


Example:

.. figure:: https://i.imgur.com/KKlSb49.png
   :alt: example

Instead of a dice code you can also put "stats" or "dir" for a stats roll or direction roll respectively.

Installation
------------

Pip install
~~~~~~~~~~~

**System-wide install** *(sudo)*

.. code:: sh

    pip install dice-roller

**User install** *(no sudo)*

.. code:: sh

    pip install --user dice-roller

    # Add local 'pip' to PATH:
    # (In your .bashrc, .zshrc etc)
    export PATH="${PATH}:${HOME}/.local/bin/"

Manual/Git install
~~~~~~~~~~~~~~~~~~

.. code:: sh

    git clone https://git.xirion.net/victor/dice-roller/
    cd dice-roller
    pip3 install --user .

    # Add local 'pip' to PATH:
    # (In your .bashrc, .zshrc etc)
    export PATH="${PATH}:${HOME}/.local/bin/"

OS/Distro Packages
~~~~~~~~~~~~~~~~~~

Arch Linux
^^^^^^^^^^

``dice-roller`` is available on the AUR as ``dice-roller-git``.
