import sys

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,-1,-1,1,1]

def count_adj(m, i, j):
    res = 0
    for d in range(len(dx)):
        f = 0
        while True:
            f += 1
            i1, j1 = i+dx[d]*f, j+dy[d]*f
            if i1 < 0 or j1 < 0 or i1 >= len(m) or j1 >= len(m[i]) or m[i1][j1] == 'L': break
            if m[i1][j1] == '#':
                res += 1
                break
    return res


m = [l.rstrip() for l in sys.stdin]

stable = False
while not stable:
    m2 = []
    stable = True
    for i in range(len(m)):
        m2.append([])
        for j in range(len(m[i])):
            if m[i][j] == 'L' and count_adj(m, i, j)  == 0:
                m2[i].append('#')
                stable = False
            elif m[i][j] == '#' and count_adj(m, i, j) >= 5:
                m2[i].append('L')
                stable = False
            else:
                m2[i].append(m[i][j])
    m = m2

print(sum(mi.count('#') for mi in m))
