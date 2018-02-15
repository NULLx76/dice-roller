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


# Takes in a string with dice and returns the rolled dice and the sum
def dice_roller(input_text):
    # Definitions
    r_dice = re.compile('\d*d\d+')               # Regex for detecting dice notation
    rolls = []                                   # List of the rolls (2D list)

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

    # Regex the input and automatically run the dice rolling code when dice notation is detected
    output = eval(r_dice.sub(roll_dice, input_text))

    return output, rolls


# If no arguments are given
if len(sys.argv) is 1:
    print('Syntax is: roll <dice_code>')
    sys.exit(2)

input_list = sys.argv[1:]                    # Command line input (is a list)
input_string = ''.join(input_list)           # Push everything together in a string

# Run the function
run_dice_roller = dice_roller(input_string)

# Print the results
print("Total: " + str(run_dice_roller[0]))
print("Rolls: " + str(run_dice_roller[1]))
