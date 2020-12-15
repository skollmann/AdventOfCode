import sys

nums = [int(n) for n in sys.stdin.readline().rstrip().split(',')]

lastidx = {}
for i in range(2020):
    if i >= len(nums)-1:
        if nums[i] in lastidx:
            num = i - lastidx[nums[i]]
        else:
            num = 0
        nums.append(num)
    lastidx[nums[i]] = i

print(nums[2019])
