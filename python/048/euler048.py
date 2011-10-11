if __name__ == '__main__':

    result = 0
    limit = 1000

    result = sum([x**x for x in xrange(1, limit+1)])

    print "RESULT=%s" % (str(result)[-10:])
