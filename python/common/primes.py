from search import *

def listprimes(target):
    primes = [2]

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

    primes.extend([x for x in odds if x])
    return primes

def isprime(num, klist):
    '''return True if the number is prime, false otherwise'''
    if num < 2:
        return False
    if num == 2:
        return True
    if (( num / 2 ) * 2 == num):
        return False
    else:
        for k in klist[1:]:
            if k == num:
                return True

            elif (( num / k ) * k == num ):
                return False
        return True

def primefact(n, primes):
    val = n
    dicfac = {}

    if binary_search(n, primes) > 0:
        return {n: 1}

    for p in primes:
        while val % p == 0:
            val = val / p

            try:
                dicfac[p] += 1
            except KeyError:
                dicfac[p] = 1

        if binary_search(val, primes) > 0:
            try:
                dicfac[val] += 1
                return dicfac
            except KeyError:
                dicfac[val] = 1
                return dicfac

        if val == 1:
            break

    return dicfac

def loadprimes(limit=2, count=-1):
    f = open("./common/primes.txt", "r")
    primes = []

    if count < 0:
        for line in f.readlines():
            if int(line) > limit:
                break

            primes.append(int(line))
    else:
        for idx, line in enumerate(f.readlines()):
            if idx >= count:
                break

            primes.append(int(line))

    f.close()
    return primes

def saveprimes(limit):
    f = open("./common/primes.txt", "w")

    f.writelines(["%s\n" % (prime) for prime in listprimes(limit)])

    f.close

