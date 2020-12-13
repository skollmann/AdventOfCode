import sys

ts = int(sys.stdin.readline().rstrip())
schedules = [int(s) for s in filter(lambda s: s != 'x', sys.stdin.readline().rstrip().split(','))]

w = 0
while True:
    for s in schedules:
        if (ts+w)%s == 0:
            print(s*w)
            sys.exit(0)
    w += 1
