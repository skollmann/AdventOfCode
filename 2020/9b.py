import sys
from collections import deque,defaultdict

cnts = defaultdict(int)
all_nums = []
nums = deque()
sums = [0]
P = 25
target = None
for line in sys.stdin:
    n = int(line.rstrip())
    sums.append(sums[-1] + n)
    all_nums.append(n)

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

        if not found and not target:
            target = n

        old = nums.popleft()
        cnts[old] -= 1
        if cnts[old] == 0:
            del cnts[old]

    cnts[n] += 1

N = len(all_nums)
for i in range(N):
    for j in range(i+1,N):
        s = sum(all_nums[i:j+1])
        if s == target:
            print(min(all_nums[i:j+1]) + max(all_nums[i:j+1]))
