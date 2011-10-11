from itertools import permutations
from math import floor, ceil

def iscube(x):
    return (int(round(x**(1.0/3))))**3 == x

def findcube(digits):
    start = int(ceil((10**(digits-1))**(1.0/3)))
    end = int(ceil((10**digits)**(1.0/3)))

    targetperm = 5

    print ". Check %d digits (from %d to %d)" % (digits, start, end-1)

    cubes = set([x**3 for x in range(start,end)])

    for val in range(start, end):
        print val

        permuts = set([int("".join(p)) for p in permutations(str(val**3)) if p[0] != '0'])

        if len(cubes & permuts) == targetperm:
            return val

    return 0

if __name__ == '__main__':
    digits = 8
    result = 0

    while result == 0:
        result = findcube(digits)
        digits += 1

    print "RESULT=%d" % (result)
