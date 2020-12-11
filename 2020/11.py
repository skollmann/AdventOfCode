import sys

def count_adj(m, i, j):
    res = 0
    for i1 in range(max(0,i-1), min(len(m),i+2)):
        for j1 in range(max(0,j-1), min(len(m[i]),j+2)):
            if i == i1 and j == j1: continue
            if m[i1][j1] == '#': res += 1
    return res


m = [l.rstrip() for l in sys.stdin]

stable = False
while not stable:
    m2 = []
    stable = True
    for i in range(len(m)):
        m2.append([])
        for j in range(len(m[i])):
            adj = count_adj(m, i, j)
            if m[i][j] == 'L' and adj == 0:
                m2[i].append('#')
                stable = False
            elif m[i][j] == '#' and adj >= 4:
                m2[i].append('L')
                stable = False
            else:
                m2[i].append(m[i][j])
    m = m2

print(sum(mi.count('#') for mi in m))
