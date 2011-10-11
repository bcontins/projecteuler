from itertools import permutations

import re

allprods = []

def testprod(stp):
    #print stp
    mmb = stp.split("=")
    if eval(mmb[0]) == int(mmb[1]):
        return int(mmb[1])
    else:
        return 0

def checkvalid(stp):
    if stp.find("=") > 6:
        return False
    elif stp.find("=") < 5:
        return False
    elif stp.find(">") > 2:
        return False
    elif stp.find(">") < 1:
        return False
    elif stp.find("=")-stp.find("*") < 2:
        return False
    else:
        return True

if __name__ == '__main__':
    result = 0

    for stper in permutations("123456789=*"):
        string = "".join(stper)
        print string

        if checkvalid(string):
            prod = testprod(string+digits[0])
            if prod > 0 and prod not in allprods:
                print ". Found new product: %s" % (string+digits[0])
                allprods.append(prod)
                result += prod

    print "RESULT=%d" % (result)

