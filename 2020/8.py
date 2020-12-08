#!/usr/bin/python3

import sys

prog = []
for line in sys.stdin:
    code, arg = line.rstrip().split(' ')
    prog.append((code, int(arg)))

used = [False for _ in range(len(prog))]
acc = 0
pc = 0
while True:
    if used[pc]:
        print(acc)
        break
    used[pc] = True
    code, arg = prog[pc]
    if code == 'acc':
        acc += arg
        pc += 1
    elif code == 'jmp':
        pc += arg
    else:
        pc += 1
