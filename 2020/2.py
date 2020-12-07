import re
import sys

def solve(line):
    t = re.split('-|:| ', line)
    mini,maxi,ch,passwd = int(t[0]),int(t[1]),t[2],t[4]
    cnt = passwd.count(ch)
    return mini <= cnt <= maxi

cnt = 0
for line in sys.stdin:
    if solve(line):
        cnt += 1

print(cnt)
