import sys

def seatid(seat):
    return int(seat.rstrip().replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)

seats = sorted(map(seatid, sys.stdin))

prev = seats[0]
for s in seats:
    if s > prev + 1:
        print(s-1)
    prev = s
