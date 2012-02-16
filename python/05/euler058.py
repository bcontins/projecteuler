import time

from primes import *
from search import *

if __name__ == '__main__':
    size = 7
    val = 49
    limit = 1000000

    alldiag = 13
    primediag = 8
    
    primes = listprimes(limit)
    lenprim = len(primes)

    print ". Listed %d primes" % (lenprim)

    print ". Ratio for size %d: %f" % (size, float(primediag)/alldiag)

    while float(primediag)/alldiag > 0.10:
        size += 2
        for i in range(4):
            val += size - 1
            if val < limit and binary_search(primes, val) >= 0:
                #print ". Found prime search: %d" % (val)
                primediag += 1

            elif isprime(val, primes):
                #print ". Found prime isprime: %d" % (val)
                primediag += 1

        alldiag += 4

        #if val > limit**2:
        #    print "! Not enough primes: %d" % (val)
        #    time.sleep(5)

    print ". Ratio for size %d: %f" % (size, float(primediag)/alldiag)


    print "RESULT=%d" % (size)

