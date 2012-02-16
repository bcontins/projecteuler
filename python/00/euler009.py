if __name__ == '__main__':

    found = False

    for a in xrange(1, 333):
        for b in xrange(a+1, (1000-a)/2):
            c = 1000 - a - b

            if a*a + b*b == c*c:
                found = True               
                break

        if found:
            break

    print "RESULT=%d,%d,%d" % (a, b, c)
    print "RESULT=%d" % (a*b*c)

