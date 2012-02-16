if __name__ == '__main__':
    power = 5
    result = 0

    for num in range(2, 1000000):
        sumpow = 0
        for digit in "%s" % (num):
            sumpow += int(digit)**power

        if num == sumpow:
            print ". Found one: %d" % (num)
            result += num

    print "RESULT=%d" % (result)

