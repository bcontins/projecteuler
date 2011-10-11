from decimal import *

if __name__ == '__main__':
    maxcycle = 0
    maxnum = 0

    getcontext().prec = 5001

    for num in range(2, 1000):
        frac = Decimal(1) / Decimal(num)
        decim = str(frac)[2:-1]

        if len(decim) < 5000:
            print ". %03d: Finite decimal" % (num)
            continue

        if decim[-100:] == decim[-100]*100:
            print ". %03d: Single digit cycle" % (num)
            continue

        for cy in range(2, 2001):
            if decim[-2*cy:] == decim[-1*cy:]*2:
                print ". %03d: Found cycle of %d" % (num, cy)

                if cy > maxcycle:
                    maxcycle = cy
                    maxnum = num

                    print decim
                break



    print "RESULT=%d with %d" % (maxnum, maxcycle)

