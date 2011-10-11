if __name__ == '__main__':
    maxdiv = 20
    seed = 1*2*3*5*7*11*13*17*19
    number = seed
    
    while True:
        valid = True
        
        for div in xrange (1,maxdiv+1):
            if number % div != 0:
                valid = False
                break
                
        if valid:
            break
        
        number+=seed
                    
    print "RESULT=%s" % (number)
