from primes import *
from search import *

from operator import mul

if __name__ == '__main__':
    limit = 10000000
    primes = listprimes(limit)

    minratio = 10.0
    minn = 0

    print ". Loaded %d primes" % (len(primes))

    for n in range(2, limit):
        phi = n
        
        for fact in primefact(n, primes):
            phi *= (1.0 - (1.0/int(fact)))

        if sorted(str(n)) == sorted(str(int(phi))):
            ratio = float(n)/phi
            print "%d -> %d = %f" % (n, phi, ratio)

            if ratio < minratio:
                minratio = ratio
                minn = n

    print "RESULT=%d" % (minn)
