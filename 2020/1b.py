import sys

a = []
for line in sys.stdin:
    a.append(int(line.rstrip()))

b = [False for _ in range(2020)]
for n in a:
    b[n] = True

for n in a:
    for m in a:
        if 0 <= 2020-n-m <= 2020 and b[2020-n-m]:
            print(n, m, 2020-n-m, n*m*(2020-n-m))

