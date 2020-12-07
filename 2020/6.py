#!/usr/bin/python3

import sys
from itertools import chain

total = 0
group = set()
for line in chain(sys.stdin, ['']):
    if line.rstrip():
        for c in line.rstrip():
            group.add(c)
    else:
        total += len(group)
        group = set()

print(total)
