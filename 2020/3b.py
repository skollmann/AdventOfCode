import sys

def solve():
    m = []
    for line in sys.stdin:
        line = line.rstrip()
        if line:
            m.append(line)

    res = 1
    for dx,dy in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        x, y = 0, 0
        cnt = 0
        while y < len(m):
            line = m[y]
            if x >= len(line): x -= len(line)
            if line[x] == '#': cnt += 1
            y += dy
            x += dx
        res *= cnt

    return res

print(solve())
