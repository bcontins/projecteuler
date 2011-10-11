from itertools import combinations, permutations

from primes import *
from search import *

def combiprimes(primes, combi):
    for pair in permutations(combi, 2):
        #print int("%d%d" % (pair[0], pair[1]))

        if binary_search(primes, int("%d%d" % (pair[0], pair[1]))) < 0:
            return False

    return True

if __name__ == '__main__':
    primecount = 5
    limit = 1000

    primes = [3] + listprimes(limit)[3:]
    testprimes = listprimes(limit*limit)

    for primeset in combinations(primes, primecount):
        print primeset

        if combiprimes(testprimes, primeset):
            break

        if primeset == (3,7,109,673):
            time.sleep(10)

    print "RESULT=%d" % (sum(primeset))
