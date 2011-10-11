import re

from primes import *

def cycperms(num):
    tabc = [num]
    snum = str(num)

    for idx in range(1, len(snum)):
        tabc.append(int(snum[idx:]+snum[:idx]))

    return list(set(tabc))

if __name__ == '__main__':
    circular = [2, 5]

    primes = listprimes(1000000)

    print ". Primes listed: %d" % (len(primes))

    pattern = re.compile("[024568]")

    for i, num in enumerate(primes):
        if i % 1000 == 0:
            print ". Processed %d" % (i)

        allprime = True
        snum = str(num)

        if pattern.search(snum):
            continue
        elif num in circular:
            continue
        else:
            for idx in range(1, len(snum)):
                if int(snum[idx:]+snum[:idx]) not in primes:
                    allprime = False

            if allprime:
                cyc = cycperms(num)
                print ". Found new circle: %s" % (str(cyc))
                circular.extend(cyc)

    #print circular

    print "RESULT=%d" % (len(circular))

