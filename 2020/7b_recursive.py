import sys
import re
from collections import defaultdict

def dfs(curr, edges):
    res = 1
    for cnt, col in edges[curr]:
        res += cnt*dfs(col, edges)
    return res

edges = defaultdict(list)
for line in sys.stdin:
    if not line.strip(): continue
    m = re.match('^(.*) bags contain (.*)\\.', line)
    color1, g2 = m.groups()
    if g2 != 'no other bags':
        for contained in g2.split(', '):
            m2 = re.match('^(\\d+) (.*) bags?$', contained)
            cnt, color2 = m2.groups()
            edges[color1].append((int(cnt), color2))

print(dfs('shiny gold', edges)-1)
