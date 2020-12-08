#!/usr/bin/python3

import sys

prog = []
for line in sys.stdin:
    op, arg = line.rstrip().split(' ')
    prog.append((op, int(arg)))

used = [False for _ in range(len(prog))]
acc = 0
pc = 0
while True:
    if used[pc]:
        print(acc)
        break
    used[pc] = True
    op, arg = prog[pc]
    if op == 'acc':
        acc += arg
        pc += 1
    elif op == 'jmp':
        pc += arg
    else:
        pc += 1
