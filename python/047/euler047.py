from primes import *

if __name__ == '__main__':

    limit = 1000000
    size = 4

    primes = listprimes(limit)
    valids = []
    consec = False

    print ". Listed %d primes" % (len(primes))

    for current in range(2, limit):
        divis = []
        idx = 0
        num = current

        while num != 1:
            if num % primes[idx] == 0:
                divis.append(primes[idx])
                num /= primes[idx]
            else:
                idx += 1

        if len(set(divis)) == size:
            valids.append(current)
            consec = True

            if len(valids) == size:
                break
        elif consec:
            valids = []
            consec = False

    print "RESULT=%s" % (str(valids))
