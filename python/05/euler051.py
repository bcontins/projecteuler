from itertools import combinations

from primes import *
from search import *

def searchresult(digits, family):
    for value in primes:
        #print ". Testing %d" % (value)

        for replcount in range(1, digits, 2):
            #print ". Trying to replace %d" % (replcount)

            for replpos in combinations(range(digits-1), replcount):
                #print " Replacing positions %s" % (str(replpos))

                countprime = 0
                tested = list(str(value))

                if replpos[0] == 0:
                    replvals = "123456789"
                else:
                    replvals = "0123456789"

                for replval in replvals:
                    for idxperm in replpos:
                        tested[idxperm] = replval

                    #print tested

                    if binary_search(primes, int("".join(tested))) >= 0:
                        countprime += 1
                        if countprime == 1:
                            result = int("".join(tested))

                if countprime >= family:
                    return result, replpos

    return 0, ()

if __name__ == '__main__':
    family = 8
    digits = 6
    result = 0

    while result == 0:
        primes = [x for x in listprimes(10**digits) if x >= 10**(digits-1)]

        print ". Testing %d digits" % (digits)

        result, replpos = searchresult(digits, family)
        digits += 1

    print "RESULT=%d" % (result)

