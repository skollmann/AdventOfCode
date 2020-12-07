#!/usr/bin/python3
import sys
import re

def check():
    names = set()
    eof = True
    for lin in sys.stdin:
        eof = False
        lin = lin.rstrip()
        if lin:
            for field in lin.split(' '):
                tok = field.split(':')
                name,val = tok[0],tok[1]
                names.add(name)
                if name == 'byr':
                    if len(val) != 4 or not (1920 <= int(val) <= 2002): return False
                if name == 'iyr':
                    if len(val) != 4 or not (2010 <= int(val) <= 2020): return False
                if name == 'eyr':
                    if len(val) != 4 or not (2020 <= int(val) <= 2030): return False
                if name == 'hgt':
                    m = re.match('^(\\d+)(cm|in)$', val)
                    if not m:
                        return False
                    h = int(m.group(1))
                    if m.group(2) == 'cm':
                        if not (150 <= h <= 193): return False
                    elif not (59 <= h <= 76): return False
                if name == 'hcl':
                    if not re.match('^#([0-9a-f]){6}$', val): return False
                if name == 'ecl':
                    if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', val): return False
                if name == 'pid':
                    if not re.match('^[0-9]{9}$', val): return False
        else:
            names.add('cid')
            return len(names) == 8
    if eof:
        return None

def solve():
    validcnt = 0
    while True:
        c = check()
        if c is None:
            return validcnt
        if c:
            validcnt += 1


print(solve())
