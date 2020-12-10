import sys

volts = []
for line in sys.stdin:
    volts.append(int(line.rstrip()))

volts.sort()
cnts = [0 for _ in range(volts[-1]+1)]
cnts[0] = 1
for v in volts:
    cnts[v] = sum(cnts[max(0,v-3):v])

print(cnts[-1])
