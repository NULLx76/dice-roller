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

# Global definitions (Step 0)
r_dice = re.compile("\d*d\d+")

# Input (Step 1)
input_list = sys.argv[1:]                    # Command line input (is a list)
input_string = ''.join(input_list)           # Push everything together in a string
rolls = []                                   # List of the rolls (2D list)

# Scan and replace dice codes (Step 2 and 3)


# dice rolling code


def roll_dice(d):
    result = 0
    dice = d.group(0)
    dice_split = dice.split("d")
    times = 1 if dice_split is '' else int(dice_split[0])
    sides = int(dice_split[1])

    for t in range(times):
        roll = random.randrange(1, sides+1)
        rolls.append(str(roll) + "/" + str(sides))
        result += roll

    return str(result)


output = r_dice.sub(roll_dice, input_string)

print("Total: " + str(eval(output)))
print("Rolls: " + str(rolls))
