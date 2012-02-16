import re

if __name__ == '__main__':
    decs = ""
    num = 1
    result = 1

    while len(decs) < 1000000:
        decs += str(num)
        num += 1

    for exp in range(1, 7):
        result *= int(decs[10**exp - 1])

    print "RESULT=%d" % (result)

