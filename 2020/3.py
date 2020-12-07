import sys

def solve():
    y = 0
    cnt = 0
    for line in sys.stdin:
        line = line.rstrip()
        if not line: continue
        if y >= len(line): y -= len(line)
        if line[y] == '#': cnt += 1
        y += 3
    return cnt

print(solve())
