#!/usr/bin/env python3
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

    t_roll = 0
    roll = 0
    rolls = []

    times = int(args[0])

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

    while times > 0:
        t_roll += random.randrange(1, sides)
        roll += t_roll
        rolls.append(t_roll)
        times -= 1

    output = roll + operation

    return output, rolls


rolling = roll_dice(sys.argv[1:])
print("Total: " + str(rolling[0]) + "\nRolls: " + str(rolling[1]))

