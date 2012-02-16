from itertools import combinations, permutations
import time
from primes import *
from search import *

def testpair(primes, pair):
    if binary_search(int("%d%d" % (pair[0], pair[1])), primes) < 0:
        return False

    elif binary_search(int("%d%d" % (pair[1], pair[0])), primes) < 0:
        return False

    return True

def testcombi(primes, combi, add):
    for first in combi:
        if first == add:
            return False

        elif binary_search(int("%d%d" % (first, add)), primes) < 0:
            return False

        elif binary_search(int("%d%d" % (add, first)), primes) < 0:
            return False

    return True

def testall():
    limit = 10000
    primes = loadprimes(limit)
    combprimes = loadprimes(limit**2)

    for pair in combinations(primes, 2):
        #print pair
        if not testpair(combprimes, pair):
            continue

        maxpair = max(pair)

        for third in primes:
            if third < maxpair:
                continue

            #print pair+(third,)
            if not testcombi(combprimes, pair, third):
                continue

            triplet = pair + (third,)
            maxtrip = max(triplet)

            for fourth in primes:
                if fourth < maxtrip:
                    continue

                #print triplet + (fourth,)
                if not testcombi(combprimes, triplet, fourth):
                    continue

                quartet = triplet + (fourth,)
                maxquart = max(quartet)

                print quartet

                for fifth in primes:
                    if fifth < maxquart:
                        continue

                    if testcombi(combprimes, quartet, fifth):
                        return quartet + (fifth,)

    return ()

if __name__ == '__main__':

    quintet = testall()

    print "RESULT=%d %s" % (sum(quintet), str(quintet))
