from primes import *

if __name__ == '__main__':

    result = 0
    limit = 10000

    primes = listprimes(limit)
    oddcompo = set(xrange(3, limit, 2)).difference(set(primes))

    for num in oddcompo:
        for pri in primes:
            isconject = False

            if pri >= num:
                break

            diff = num - pri

            if diff % 2 != 0:
                continue

            root = (diff / 2)**0.5

            if int(root) == root:
                isconject = True
                break

        #print "%d = %d + 2 x %d**2" % (num, pri, root)

        if not isconject:
            result = num
            break

    print "RESULT=%d" % (result)
