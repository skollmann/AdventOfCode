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
            m2 = re.match('^\\d+ (.*) bags?$', contained)
            color2 = m2.group(1)
            edges[color2].append(color1)

q = deque(['shiny gold'])
vis = set()
while q:
    v = q.pop()
    if v in vis: continue
    vis.add(v)
    for e in edges[v]:
        q.append(e)

print(len(vis)-1)

