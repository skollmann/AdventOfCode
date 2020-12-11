import sys

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,-1,-1,1,1]

def get_neighbors(m, i, j):
    res = []
    for d in range(len(dx)):
        f = 1
        while True:
            i1, j1 = i+dx[d]*f, j+dy[d]*f
            if i1 < 0 or j1 < 0 or i1 >= len(m) or j1 >= len(m[i]):
                break
            if m[i1][j1] == 'L':
                res.append((i1, j1))
                break
            f += 1
    return res

def count_adj(neighbors):
    res = 0
    for i1, j1 in neighbors:
        if m[i1][j1] == '#':
            res += 1
    return res

m = [list(l.rstrip()) for l in sys.stdin]
R, C = len(m), len(m[0])
neighbors = [[get_neighbors(m, i, j) for j in range(C)] for i in range(R)]

stable = False
while not stable:
    m2 = []
    stable = True
    for i in range(R):
        m2.append([])
        for j in range(C):
            if m[i][j] == 'L' and count_adj(neighbors[i][j])  == 0:
                m2[i].append('#')
                stable = False
            elif m[i][j] == '#' and count_adj(neighbors[i][j]) >= 5:
                m2[i].append('L')
                stable = False
            else:
                m2[i].append(m[i][j])
    m = m2

print(sum(mi.count('#') for mi in m))
