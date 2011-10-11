from primes import *

if __name__ == '__main__':
    maxidx = 0
    maxa = 0
    maxb = 0
    listb = []

    primes = listprimes(1000000)

    for i in primes:
        if i > 1000:
            break
        listb.append(i)

    for a in range(-999, 1000, 2):
        print ". Progress %d" % (a)

        for b in listb:
            idx = 0
            while True:
                val = idx**2 + a*idx + b
                if val < 0 or val not in primes:
                    if idx > maxidx:
                        maxidx = idx
                        maxa = a
                        maxb = b
                        print ". New best: %d/%d at %d" % (maxa, maxb, maxidx)
                    #print ". Coefs %d/%d failed for %d" % (a, b, idx)
                    break
                idx += 1

    print "RESULT=%d (%d/%d at %d)" % (maxa*maxb, maxa, maxb, maxidx)

