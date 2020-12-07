#!/usr/bin/python3
import sys

def solve():
    validcnt = 0
    names = set()
    for lin in sys.stdin:
        lin = lin.rstrip()
        if lin:
            for field in lin.split(' '):
                name = field.split(':')[0]
                names.add(name)
        else:
            names.add('cid')
            if len(names) == 8:
                validcnt += 1
            names = set()
    return validcnt


print(solve())
