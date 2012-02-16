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
    if len(stp) == 7:
        if "=" not in stp:
            return False
        elif stp.find("=")-stp.find("*") < 2:
            return False
        else:
            return True
    elif len(stp) == 3:
        if "*" not in stp:
            return False
        else:
            return True
    elif len(stp) == 1:
        if stp[0] in ["=", "*"]:
            return False
        else:
            return True
    elif "=" in stp and "*" not in stp:
        return False
    else:
        return True

def permuts(digits, string):
    if len(string) == 2:
        print string

    if len(string) == 10:
        prod = testprod(string+digits[0])
        if prod > 0 and prod not in allprods:
            print ". Found new product: %s" % (string+digits[0])
            allprods.append(prod)
            return prod
        else:
            return 0
    else:
        sump = 0
        for dig in digits:
            remaindigits = list(digits)
            remaindigits.remove(dig)

            if checkvalid(string+dig):
                sump += permuts(remaindigits, string+dig)

        return sump

if __name__ == '__main__':

    """
    print checkvalid("19*")
    print checkvalid("186*39=7254")
    """
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "=","*"]
    products = []

    result = permuts(digits, "")

    print "RESULT=%d" % (result)

