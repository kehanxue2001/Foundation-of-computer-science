import sys

try:
    n = int(input('Enter an integer: '))
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
