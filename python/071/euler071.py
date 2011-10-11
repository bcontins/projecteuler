def hcf(a, b):
    num = max(a, b)
    div = min(a, b)

    while div != 0:
        num, div = div, num % div

    return num

if __name__ == '__main__':

    maxdiv = 1000000
    target = float(3)/7

    result = 0
    bestdiff = 1
    bestfrac = 0.4

    for div in range(1, maxdiv+1):
        minnum = int(div * bestfrac)
        step = div % 2 == 0 and minnum % 2 == 1 and 2 or 1

        for num in range(minnum, div, step):
            if hcf(num, div) == 1:
                diff = target - float(num)/div
                if diff < 0:
                    break

                if diff < bestdiff and (num, div) != (3, 7):
                    result = num
                    bestfrac = float(num)/div
                    bestdiff = diff

    print "RESULT=%d" % (result)

