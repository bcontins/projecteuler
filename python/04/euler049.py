import itertools

from primes import *

if __name__ == '__main__':

    result = 0
    primes = set([x for x in listprimes(10000) if x > 1000])

    for subdig in [str(x) for x in range(1001, 10000, 2)]:
        #print subdig

        #listperms = set([int("".join(x)) for x in itertools.permutations(subdig)])
        listperms = set([int("".join(x)) for x in itertools.permutations(subdig) if int("".join(x)) > 1000])
        #print listperms

        valids = sorted(listperms.intersection(primes))
        
        if len(valids) < 3:
            continue

        #print valids
        for idx, low in enumerate(valids):
            for up in valids[idx+1:]:
                if (2*up - low) in valids:
                    print ". Found %s/%s/%s" % (low, up, 2*up-low)

    print "RESULT=%s" % (0)
