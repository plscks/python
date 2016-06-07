# dictionary test file
# new line function proof-of-concept
# written by plscks
import itertools
import string


d = {}
z = string.ascii_uppercase
i = 0
j = []
lines = input('how many lines: ')
lines = int(lines)
for x in range(lines):
    i = i + 1
    letter = itertools.cycle(z)
    j.append(i)
    d = dict(zip(j, letter))
    print(d[i])
