from fractions import Fraction

def fraccomp(nu1, de1, nus2, des2):
    return Fraction(nu1, de1) == Fraction(int(nus2), int(des2))

if __name__ == '__main__':

    result = Fraction(1,1)

    for de in range(10, 100):
        des = str(de)

        for nu in range(10, de):
            nus = str(nu)

            if nus[0] == des[0] and fraccomp(nu, de, nus[1], des[1]):
                print ". Found remove 1-1: %d/%d" % (nu, de)
                result *= Fraction(nu, de)

            if nus[1] == des[0] and des[1] != "0" and  fraccomp(nu, de, nus[0], des[1]):
                print ". Found remove 2-1: %d/%d" % (nu, de)
                result *= Fraction(nu, de)

            if nus[0] == des[1] and fraccomp(nu, de, nus[1], des[0]):
                print ". Found remove 1-2: %d/%d" % (nu, de)
                result *= Fraction(nu, de)

            if nus[1] == des[1] and des[1] != "0" and fraccomp(nu, de, nus[1], des[0]):
                print ". Found remove 2-2: %d/%d" % (nu, de)
                result *= Fraction(nu, de)

    print "RESULT=%s" % (str(result))

