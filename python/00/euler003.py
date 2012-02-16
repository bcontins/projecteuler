# Find the largest prime factor of a composite number.

if __name__ == '__main__':
    number = 600851475143
    maxfactor = -1
    
    # Try dividing with every possible factor factors until we reach the largest one
    # Dumb solution but takes less than 0.1 seconds to complete

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
