if __name__ == '__main__':
    result = 0

    for aa in range(1, 100):
        for bb in range(1, 100):
            digitsum = sum([int(x) for x in str(aa**bb)])

            if digitsum > result:
                result = digitsum

    print "RESULT=%d" % (result)
