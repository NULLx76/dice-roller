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

argument_string = ''.join(sys.argv[1:])
args = argument_string.split("d")

times = int(args[0])

if any('+' in s for s in args):
    args = re.split("[d+]", argument_string)
    print(args)

    sides = int(args[1])
    operation = int(args[2])
elif any('-' in s for s in args):
    args = re.split("[d-]", argument_string)
    print(args)
    times = int(args[0])
    sides = int(args[1])
    operation = - int(args[2])
else:
    times = int(args[0])
    sides = int(args[1])
    operation = 0

roll = 0
while times > 0:
    roll += random.randrange(1, sides)
    times -= 1

print("total roll: " + str(roll))
output = roll + operation

print(output)
