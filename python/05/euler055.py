def palin(val):
    return int(str(val)[::-1])

if __name__ == '__main__':

    result = 0
    limit = 10000

    for current in range(1, limit):
        num = current

        for iterat in range(51):
            num += palin(num)
            if iterat >= 50:
                result += 1

            elif num == palin(num):
                break

    print "RESULT=%d" % (result)

