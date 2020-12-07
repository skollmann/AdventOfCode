import sys
import re
from collections import defaultdict, deque

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

res = 0
q = deque([(1, 'shiny gold')])
while q:
    cnt, v = q.pop()
    for c, e in edges[v]:
        res += c*cnt
        q.append((c*cnt, e))

print(res)

