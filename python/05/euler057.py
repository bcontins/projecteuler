if __name__ == '__main__':
    limit = 1000
    num = 3
    den = 2
    result = 0

    for _ in xrange(1, limit):
        #print ". Fraction = %d/%d" % (num, den)

        if len(str(num)) > len(str(den)):
            result += 1

        num, den = num + 2*den, den + num

    print "RESULT=%d" % (result)

