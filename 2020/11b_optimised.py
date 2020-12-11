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
 
m = [list(l.rstrip()) for l in sys.stdin]
R, C = len(m), len(m[0])
cnts = [[0 if m[i][j] == 'L' else None for j in range(C)] for i in range(R)]
neighbors = [[get_neighbors(m, i, j) for j in range(C)] for i in range(R)]

added_neighbors = []
removed_neighbors = []

stable = False
while not stable:
    for i, j in removed_neighbors:
        cnts[i][j] -= 1
    for i, j in added_neighbors:
        cnts[i][j] += 1
    
    removed_neighbors = []
    added_neighbors = []

    stable = True
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'L' and cnts[i][j]  == 0:
                m[i][j] = '#'
                added_neighbors.extend(neighbors[i][j])
                stable = False
            elif m[i][j] == '#' and cnts[i][j] >= 5:
                m[i][j] = 'L'
                removed_neighbors.extend(neighbors[i][j])
                stable = False

print(sum(mi.count('#') for mi in m))
