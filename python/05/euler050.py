import itertools

from primes import *

if __name__ == '__main__':

    result = 0
    limit = 1000000
    foundit = False

    primes = listprimes(limit)

    sumpri = 0
    for idx in range(len(primes)):
        sumpri += primes[idx]
        if sumpri > limit:
            break

    maxsize = idx + 1
    print "Maximum size %d" % (maxsize)

    for size in range(maxsize, 0, -1):
        #print "Size %d" % (size)

        sumcon = sum(primes[0:size])

        for idx in range(len(primes) - size):
            #print idx
            if sumcon > limit:
                break

            if sumcon in primes:
                print ". Found sum of consecutive %d: %d = %s" % (size, sumcon, str(primes[idx:idx+size]))
                foundit = True
                break

            sumcon = sumcon - primes[idx] + primes[idx+size]

        if foundit:
            break
        #else:
        #    print ". Nothing found for %d terms" % (size)

    print "RESULT=%s" % (0)
