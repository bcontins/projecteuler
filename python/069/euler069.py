from primes import *
from operator import mul

def primefact(n, primes):
    val = n
    dicfac = {}

    if isprime(n, primes):
        return {str(n): 1}

    for p in primes:
        while val % p == 0:
            val = val / p

            try:
                dicfac[str(p)] += 1
            except KeyError:
                dicfac[str(p)] = 1

        if val == 1:
            break

    return dicfac

if __name__ == '__main__':
    limit = 1000000
    primes = listprimes(int(limit**0.5)+1)

    maxratio = 0.0
    maxn = 0

    print ". Loaded %d primes" % (len(primes))

    for n in range(2, limit):
        pfacs = primefact(n, primes)
        ratio = 1.0 / reduce(mul,[(1.0 - (1.0/int(p))) for p in pfacs])

        if ratio > maxratio:
            maxratio = ratio
            maxn = n

    print "RESULT=%d" % (maxn)
