import sys

nums = [int(n) for n in sys.stdin.readline().rstrip().split(',')]
target = 30000000

lastidx = {}
for i in range(target):
    if i >= len(nums)-1:
        if nums[i] in lastidx:
            num = i - lastidx[nums[i]]
        else:
            num = 0
        nums.append(num)
    lastidx[nums[i]] = i

print(nums[target-1])
