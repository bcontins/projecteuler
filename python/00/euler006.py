if __name__ == '__main__':

    sum = 0
    sumsquares = 0

    for number in xrange(1, 101):
        sum += number
        sumsquares += number**2

    squaresum = sum **2

    print "RESULT=%d" % (squaresum - sumsquares)
