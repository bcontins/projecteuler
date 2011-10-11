if __name__ == '__main__':

    maxmult = 6
    num = 0

    while True:
        num += 1
        if reduce(lambda x, y: x and y, [(sorted(str(num)) == sorted(str(num*mult))) for mult in range(2, maxmult+1)]):
            break

    print "RESULT=%d" % (num)
