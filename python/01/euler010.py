def primesum(target): 
    if target == 2:
        return 2
    elif target < 2:
        return 0

    odds = range(3, target+1, 2)
    mroot = target ** 0.5
    half = (target+1)/2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if odds[i]:
            j=(m*m-3)/2
            odds[j]=0
            while j<half:
                odds[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return 2 + sum([x for x in odds if x])

if __name__ == '__main__':

    print "RESULT=%d" % (primesum(2000000))

