import re

def countpossib(peri):
    possib = 0

    for a in range(1, int(peri/2)):
        for b in range(a, int(peri/2)):
            c = peri - a - b

            if a**2 + b**2 == c**2:
                #print ". Found combination {%d,%d,%d}" % (a, b, c)
                possib += 1

    return possib

if __name__ == '__main__':
    maxpossib = 0
    bestperi = 0

    for peri in range(12, 1001):
        possib = countpossib(peri)

        if possib > maxpossib:
            bestperi = peri
            maxpossib = possib

    print "RESULT=%d" % (bestperi)

