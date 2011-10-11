from itertools import permutations
from math import floor, ceil

def iscube(x):
    return (int(round(x**(1.0/3))))**3 == x

def findcube(digits):
    start = int(ceil((10**(digits-1))**(1.0/3)))
    end = int(ceil((10**digits)**(1.0/3)))

    targetperm = 5
    result = 0
    diccubes = {}

    print ". Check %d digits (from %d to %d)" % (digits, start, end-1)

    for cube in [x**3 for x in range(start,end)]:
        key = "".join(sorted(str(cube)))

        try:
            diccubes[key].append(cube)
        except KeyError:
            diccubes[key] = [cube, ]

    for key in diccubes:
        if len(diccubes[key]) == targetperm:
            if result == 0:
                result = min(diccubes[key])
            else:
                result = min(result, min(diccubes[key]))

    return result

if __name__ == '__main__':
    digits = 2
    result = 0

    while result == 0:
        result = findcube(digits)
        digits += 1

    print "RESULT=%d" % (result)
