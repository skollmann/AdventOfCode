import sys

jolts = []
for line in sys.stdin:
    jolts.append(int(line.rstrip()))

jolts.sort()

# cnts[j] = number of arrangements ending with joltage j (0 if no adapter with joltage j exists)
cnts = [0 for _ in range(jolts[-1]+1)]
cnts[0] = 1
for j in jolts:
    cnts[j] = sum(cnts[max(0,j-3):j])

print(cnts[-1])
