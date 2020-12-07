#!/usr/bin/python3

import sys
import string
from itertools import chain

total = 0
group = None
for line in chain(sys.stdin, ['']):
    if line.rstrip():
        group2 = set()
        for c in line.rstrip():
            if group is None or c in group:
                group2.add(c)
        group = group2
    else:
        total += len(group)
        group = None

print(total)
