import sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

d = 0
x = 0
y = 0

for line in sys.stdin:
    op = line[0]
    val = int(line[1:].rstrip())
    if op == 'N': 
        y += val
    elif op == 'S':
        y -= val
    elif op == 'E':
        x += val
    elif op == 'W':
        x -= val
    elif op == 'L':
        d = (d+3*(val//90))%4
    elif op == 'R':
        d = (d+1*(val//90))%4
    elif op == 'F':
        x += dx[d]*val
        y += dy[d]*val
    else:
        print('Invalid command: %s' % line)
    print(x, y, d)

print(abs(x) + abs(y))

