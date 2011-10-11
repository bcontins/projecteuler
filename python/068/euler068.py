from itertools import permutations

if __name__ == '__main__':
    maxval = 0

    for gon in permutations(range(1, 11)):
        if gon.index(10) >= 5:
            continue

        line = [[gon[0], gon[5], gon[6]],
                [gon[1], gon[6], gon[7]],
                [gon[2], gon[7], gon[8]],
                [gon[3], gon[8], gon[9]],
                [gon[4], gon[9], gon[5]]
                ]

        if not (sum(line[0]) == sum(line[1]) == sum(line[2]) == sum(line[3]) == sum(line[4])):
            continue

        if line[0][0] > line[1][0] or line[0][0] > line[2][0] or line[0][0] > line[3][0] or line[0][0] > line[4][0]:
            continue

        lineval = int("".join([str(item) for sublist in line for item in sublist]))

        maxval = max(maxval, lineval)

    print "RESULT=%d" % (maxval)

