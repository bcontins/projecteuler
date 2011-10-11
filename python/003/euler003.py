if __name__ == '__main__':
    number = 600851475143
    maxfactor = -1
    
    for factor in xrange(2, number/2):
        while number % factor == 0:
            print ". Factor found = %d" % (factor)
            number /= factor
            maxfactor = factor
            print ". Number is now = %d" % (number)

        if number == 1:
            print ". Finished dividing"
            break

    print "RESULT=%s" % (maxfactor)
