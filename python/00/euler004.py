if __name__ == '__main__':
    limit = 999
    maxpal = 0
    
    for a in xrange(1, limit+1):
        for b in xrange(1, limit+1):
            prod = str(a * b)

            if prod == prod[::-1]:
                #print ". Found palindrome: %s" % (prod)

                if int(prod) > maxpal:
                    maxpal = int(prod)
                    
    print "RESULT=%s" % (maxpal)
