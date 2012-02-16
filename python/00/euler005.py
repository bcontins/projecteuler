# What is the smallest number divisible by each of the numbers 1 to 20?

if __name__ == '__main__':
    maxdiv = 20
    seed = 1*2*3*5*7*11*13*17*19
    number = seed
    
    while True:
        valid = True
        
        # Try to divide by each number from 1 to 20
        for div in xrange (1,maxdiv+1):
            if number % div != 0:
                valid = False
                break
                
        if valid:
            break
        
        # Result will have to be a multiple of each prime number up to 20
        # So we only have to test multiples of the product of these numbers
        number+=seed
                    
    print "RESULT=%s" % (number)
