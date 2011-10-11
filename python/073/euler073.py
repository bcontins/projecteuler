def hcf(a, b):
    num = max(a, b)
    div = min(a, b)

    while div != 0:
        num, div = div, num % div

    return num

if __name__ == '__main__':

    maxdiv = 12000

    result = -1
    lowfrac = float(1)/3
    hifrac = float(1)/2

    for div in range(1, maxdiv+1):
        minnum = max(1, int(div * lowfrac)+1)
        maxnum = int(div * hifrac)+1

        step = div % 2 == 0 and minnum % 2 == 1 and 2 or 1

        for num in range(minnum, maxnum, step):
            if hcf(num, div) == 1:
                result += 1

    print "RESULT=%d" % (result)

