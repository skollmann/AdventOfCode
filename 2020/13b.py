import sys

ts = int(sys.stdin.readline().rstrip())
schedules = [0 if s == 'x' else int(s) for s in sys.stdin.readline().rstrip().split(',')]

def eea(a, b):
    """ 
    Extended euclidean algorithm. Solves the equation a*x + b*y = gcd(a,b).
    Returns {x, y, +/-gcd(a,b)}
    Assumes a, b > 0.
    """
    if a == 0: return (0, 1, b)
    x = eea(b%a, a)
    return (x[1] - b//a*x[0], x[0], x[2])


def chinese_remainder(a, m):
    """
    Returns the smallest l >= 0, such that for all i, a[i] = l (mod m[i]).
    All solutions are congruent mod m[0]*[1]*...*m[m.length-1].
    Requires all m[i] to be coprime.
    """
    M = 1
    for l in m: M *= l

    x = 0
    for i in range(len(m)):
        e = (eea(m[i], M//m[i])[1] * (M//m[i]))%M
        x = (x + a[i]*e)%M
    
    return x%M


a = []
m = []
for i, s in enumerate(schedules):
    if s != 0:
        a.append(s-i)
        m.append(s)

# Note that I'm assuming here that all m[i] are coprime, which seems to be the case in my input.
print(chinese_remainder(a, m))
