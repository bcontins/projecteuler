if __name__ == '__main__':
    fib = 0
    f1 = 1
    f2 = 1

    term = 2

    while len("%s"%fib) < 1000:
        fib = f1 + f2
        f2 = f1
        f1 = fib
        term += 1

    print "RESULT=%d(%d)" % (term, len("%s"%fib))

