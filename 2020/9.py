import sys
from collections import deque,defaultdict

cnts = defaultdict(int)
nums = deque()
P = 25
for line in sys.stdin:
    n = int(line.rstrip())

    nums.append(n)
    if len(nums) > P:
        found = False
        for n1 in cnts:
            assert cnts[n1] > 0
            if n == 2*n1:
                if n1 in cnts and cnts[n1] >= 2:
                    found = True
                    break
            else:
                if (n-n1) in cnts and cnts[n-n1] >= 1:
                    found = True
                    break

        if not found:
            print(n)
            break

        old = nums.popleft()
        cnts[old] -= 1
        if cnts[old] == 0:
            del cnts[old]

    cnts[n] += 1
