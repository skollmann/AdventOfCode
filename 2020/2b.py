import re
import sys

def solve(line):
    t = re.split('-|:| ', line)
    i1,i2,ch,passwd = int(t[0]),int(t[1]),t[2],t[4]
    return (passwd[i1-1] == ch) != (passwd[i2-1] == ch)

cnt = 0
for line in sys.stdin:
    if solve(line):
        cnt += 1

print(cnt)
