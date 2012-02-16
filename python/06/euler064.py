from math import floor, sqrt
import time

def findloop(suite):
    lens = len(suite)

    if lens % 2 != 0:
        return -1

    elif lens < 12:
        return -1

    elif lens == 12 and 12*[suite[0],] == suite:
        return 1

    elif lens == 12 and 6*suite[0:2] == suite:
        return 2

    elif lens == 12 and 4*suite[0:3] == suite:
        return 3

    elif lens == 12 and 3*suite[0:4] == suite:
        return 4

    elif lens == 20 and 4*suite[0:5] == suite:
        return 5

    elif suite[:(lens/2)] == suite[(lens/2):]:
        return lens/2

    else:
        return -1

def fractloop(num):
    suite = []
    div = 1

    roundsq = int(floor(sqrt(num)))
    integ = roundsq
    rest = roundsq

    while True:
        prevdiv = div

        div = (num - rest**2)/prevdiv
        integ = 0

        while roundsq + rest >= div:
            rest -= div
            integ += 1

        rest *= -1

        suite.append(integ)
        period = findloop(suite)

        if period > 0:
            return period

if __name__ == '__main__':
    limit = 10000
    result = 0

    for num in range(2, limit+1):
        if int(num**0.5)**2 == num:
            continue

        if fractloop(num) % 2 == 1:
            result += 1

    print "RESULT=%d" % (result)
