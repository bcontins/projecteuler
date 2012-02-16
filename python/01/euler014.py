dicloop = {}

def countchain(val):
    it = 1
    step = val

    while (step != 1):
        if step % 2 == 0:
            step /= 2
        else:
            step = 3 * step + 1

        it += 1

    return it

if __name__ == '__main__':

    result = 0
    maxchain = 0

    for init in xrange(1, 1000000):
        chain = countchain(init)
        if chain > maxchain:
            result = init
            maxchain = chain

    print "RESULT=%d" % (result)

