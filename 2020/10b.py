import sys

jolts = []
for line in sys.stdin:
    jolts.append(int(line.rstrip()))

jolts.sort()
cnts = [0 for _ in range(jolts[-1]+1)]
cnts[0] = 1
for v in jolts:
    cnts[v] = sum(cnts[max(0,v-3):v])

print(cnts[-1])
