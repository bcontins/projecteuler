if __name__ == '__main__':
    result = 0

    for num in range(1, 1000000, 2):
        sdec = str(num)
        sbin = str(bin(num))[2:]

        if sdec == sdec[::-1] and sbin == sbin[::-1]:
            print ". Found palindromic: %s/%s" % (sdec, sbin)
            result += num

    print "RESULT=%d" % (result)

