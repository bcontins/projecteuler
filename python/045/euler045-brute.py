def triang(num):
    return (num*(num+1))

def pentag(num):
    return (num*(3*num-1))/2

def hexag(num):
    return (num*(2*num-1))

if __name__ == '__main__':

    result = 0
    start = 290
    limit = 1000000

    pentagratio = [0.577350269190, 0.581898899867]
    hexagratio = [0.500000000000, 0.505000000000]

    pentags = [pentag(x) for x in range(1, int(limit*pentagratio[1])+1)]
    hexags = [hexag(x) for x in range(1, int(limit*hexagratio[1])+1)]

    print ". Listed %d pentagonals" % (len(pentags))
    print ". Listed %d hexagonals" % (len(hexags))

    for idx in range(start, limit):
        if idx % 1000 == 0:
            print ". Testing %d to %d" % (idx, idx+999)

        curtriang = (idx**2 + idx) / 2

        minpentag = int(idx * pentagratio[0]) - 1
        maxpentag = int(idx * pentagratio[1]) + 2

        minhexag = int(idx * hexagratio[0]) - 1
        maxhexag = int(idx * hexagratio[1]) + 2

        """
        print idx

        print minpentag
        print maxpentag

        print minhexag
        print maxhexag

        print curtriang
        print pentags[minpentag:maxpentag]
        print hexags[minhexag:maxhexag]
        """

        if (curtriang in pentags[minpentag:maxpentag]) and (curtriang in hexags[minhexag:maxhexag]):
            print ". Found %d at index %d" % (curtriang, idx)
            result = curtriang
            break

    print "RESULT=%d" % (result)
