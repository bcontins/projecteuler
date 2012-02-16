# Find the largest palindrome made from the product of two 3-digit numbers.

if __name__ == '__main__':
    limit = 999
    maxpal = 0
    
    # Compute all products of three digit numbers 
    for a in xrange(100, limit+1):
        for b in xrange(100, limit+1):
            prod = str(a * b)

            # If string representation of number equals its reverse, we have a palindrome
            if prod == prod[::-1]:
                if int(prod) > maxpal:
                    maxpal = int(prod)
                    
    print "RESULT=%s" % (maxpal)
