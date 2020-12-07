import sys

def seatid(seat):
    return int(seat.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)

maxi = 0 
for seat in sys.stdin:
    maxi = max(maxi, seatid(seat.rstrip()))

print(maxi)
