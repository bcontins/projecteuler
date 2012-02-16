if __name__ == '__main__':
    result = 0

    for char in "%d" % (2**1000):
        result += int(char)

    print "RESULT=%d" % (result)

