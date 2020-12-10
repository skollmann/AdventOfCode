import sys

joltages = []
for line in sys.stdin:
    joltages.append(int(line.rstrip()))

prev = 0
diffs = [0,0,0,1]
for j in sorted(joltages):
    if j-prev <= 3:
        diffs[j-prev] += 1
    prev = j

print(diffs[1]*diffs[3])
