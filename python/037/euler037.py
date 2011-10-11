import re

from primes import *

if __name__ == '__main__':
    primes = listprimes(1000000)
    listtrunc = [23]

    print ". Primes listed: %d" % (len(primes))

    pattern = re.compile("[02468]")

    for i, num in enumerate(primes[4:]):
        snum = str(num)

        if pattern.search(snum):
            continue

        istrunc = True

        for idx in range(1, len(snum)):
            if int(snum[idx:]) not in primes:
                istrunc = False
                break
            if int(snum[:-1*idx]) not in primes:
                istrunc = False
                break

        if istrunc:
            print ". Found truncable: %d" % (num)
            listtrunc.append(num)
            if len(listtrunc) == 11:
                print ". Found all truncables"
                break

    print "RESULT=%d" % (sum(listtrunc))

