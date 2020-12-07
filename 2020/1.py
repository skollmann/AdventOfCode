import sys

a = []
for line in sys.stdin:
    a.append(int(line.rstrip()))

b = [False for _ in range(2020)]
for n in a:
    if n == 1010 and b[n]:
        print(1010*1010)
        break
    b[n] = True

for n in a:
    if n != 1010 and b[2020-n]:
        print(n*(2020-n))

