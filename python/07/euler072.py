from primes import *
from operator import mul

def phi(n):
    phival = n
    for fact in primefact(n, primes):
        phival *= (1.0 - (1.0/int(fact)))

    return int(phival)

if __name__ == '__main__':
    limit = 1000
    primes = listprimes(limit)

    print ". Loaded %d primes" % (len(primes))

    result = 0

    for div in range(2, limit+1):
        if div % 1000 == 0:
            print div

        result += phi(div)

    print "RESULT=%d" % (result)

