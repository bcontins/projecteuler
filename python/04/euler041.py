from itertools import permutations
import math

from primes import *

if __name__ == '__main__':
    #

    listdig = "123456789"
    maxprim = 0

    for nbdig in range (4, 10):
        print ". Checking numbers with %d digits" % (nbdig)

        klist = listprimes(int(math.sqrt(10**nbdig+1)))

        for possib in permutations(listdig[:nbdig]):
            if possib[-1] in "24568":
                continue

            val = int("".join(possib))

            if isprime(val, klist) and val > maxprim:
                print ". Found new maximum pandigital prime: %d" % (val)
                maxprim = val

    print "RESULT=%d" % (maxprim)

