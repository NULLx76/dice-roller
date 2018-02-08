#!/usr/bin/env python3
# coding: utf-8
import sys
import re
import random

try:
    # Use the system PRNG if possible
    random = random.SystemRandom()
except NotImplementedError:
    import warnings
    warnings.warn("A secure pseudo-random number generator is not available "
                  "on your system. Falling back to Mersenne Twister.")


def roll_dice(args_list):
    if not isinstance(args_list, str):
        args_string = ''.join(args_list)
    else:
        args_string = args_list

    args = args_string.split("d")

    # Without times specified treat it is one
    if args[0] is not '':
        times = int(args[0])
    else:
        times = 1

    # Support for adding or subtracting by suffixing minus or plus (i.e. 4d6+12)
    if any('+' in s for s in args):
        args = re.split("[d+]", args_string)
        sides = int(args[1])
        operation = int(args[2])
    elif any('-' in s for s in args):
        args = re.split("[d-]", args_string)
        sides = int(args[1])
        operation = - int(args[2])
    else:
        sides = int(args[1])
        operation = 0

    # rolling the dice and keeping track of the rolls
    roll = 0
    rolls = []
    for n in range(times):
        t_roll = random.randrange(1, sides)
        roll += t_roll
        rolls.append(t_roll)

    # Add any operation (+ or -)
    output = roll + operation

    # Returns total and individual rolls
    return output, rolls


rolling = roll_dice(sys.argv[1:])
print("Total: " + str(rolling[0]) + "\nRolls: " + str(rolling[1]))
