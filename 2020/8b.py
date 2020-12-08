#!/usr/bin/python3

import sys

def execute(prog):
    used = [False for _ in range(len(prog))]
    acc = 0
    pc = 0
    while pc < len(prog):
        if used[pc]:
            return None
        used[pc] = True
        op, arg = prog[pc]
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        else:
            pc += 1
    return acc

def execute_modified(prog, i, new_op):
    old_op = prog[i][0]
    prog[i][0] = new_op
    res = execute(prog)
    prog[i][0] = old_op
    return res

prog = []
for line in sys.stdin:
    op, arg = line.rstrip().split(' ')
    prog.append([op, int(arg)])

for i in range(len(prog)):
    if prog[i][0] in ['jmp', 'nop']:
        acc = execute_modified(prog, i, 'nop' if prog[i][0] == 'jmp' else 'jmp')
        if acc is not None:
            print(acc)
