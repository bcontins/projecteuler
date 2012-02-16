if __name__ == '__main__':
    result = 0

    for power in range(1, 30):
        for num in range(1,10):
            if len(str(num**power)) == power:
                #print ". Found %d**%d" % (num, power)
                result += 1

    print "RESULT=%d" % (result)

