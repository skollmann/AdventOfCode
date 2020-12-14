import sys
import re

ormask = 0
andmask = 0 

mem = {}

for line in sys.stdin:
    if line.startswith('mask'):
        mask = line.rstrip()[7:]
        andmask = int(mask.replace('X', '1'), 2)
        ormask = int(mask.replace('X', '0'), 2)
    else:
        m = re.match('mem\\[(\\d+)\\] = (\\d+)', line)
        addr = int(m.group(1))
        val = (int(m.group(2)) & andmask) | ormask
        mem[addr] = val

for k in mem:
    print(k, mem[k])

print(sum(mem.values()))
