from math import sqrt
import time

def issquare(val):
    return (int(sqrt(val)))**2 == (val)

def solvedio(mult):
    x = 2

    while True:
        if ((x**2 - 1) % mult == 0) and (int(sqrt((x**2 - 1) / mult)))**2 == ((x**2 - 1) / mult):
            return x

        x += 1

if __name__ == '__main__':
    result = 0
    maxdior = 0
    limit = 1001

    print solvedio(13)

    for mult in range(2, limit):
        if issquare(mult):
            continue

        print mult

        dior = solvedio(mult)

        print ". %d" % (dior)

        if dior > maxdior:
            maxdior = dior
            result = mult

    print "RESULT=%d" % (result)

