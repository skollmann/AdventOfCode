import sys

x, y = 0, 0
wx, wy = 10, 1

for line in sys.stdin:
    op = line[0]
    val = int(line[1:].rstrip())
    if op == 'N': 
        wy += val
    elif op == 'S':
        wy -= val
    elif op == 'E':
        wx += val
    elif op == 'W':
        wx -= val
    elif op == 'L':
        for i in range(val//90):
            wx, wy = -wy, wx
    elif op == 'R':
        for i in range(val//90):
            wx, wy = wy, -wx
    elif op == 'F':
        x += wx*val
        y += wy*val
    else:
        print('Invalid command: %s' % line)
    print(x, y, wx, wy)

print(abs(x) + abs(y))

