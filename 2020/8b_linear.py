#!/usr/bin/python3

import sys
from collections import deque

prog = []
for line in sys.stdin:
    op, arg = line.rstrip().split(' ')
    prog.append((op, int(arg)))

q = deque([(0, False, 0)])
n = len(prog)
visited = [[False, False] for _ in range(n)]
while q:
    pc, used_flipped_op, acc = q.pop()
    if pc == n:
        print(acc)
        break
    if visited[pc][int(used_flipped_op)]:
        continue
    visited[pc][int(used_flipped_op)] = True
    op, arg = prog[pc]
    if op == 'acc':
        q.append((pc+1, used_flipped_op, acc+arg))
    elif op == 'jmp':
        q.append((pc+arg, used_flipped_op, acc))
        if not used_flipped_op:
            q.append((pc+1, True, acc))
    else:
        q.append((pc+1, used_flipped_op, acc))
        if not used_flipped_op:
            q.append((pc+arg, True, acc))

