def findfract(integ, seqfrac):
    num = 1

    den = seqfrac[-1]

    for val in seqfrac[-2::-1]:
        num, den = den, (val * den + num)

    num = integ * den + num

    return num, den

if __name__ == '__main__':
    target = 100
    seqfrac = []

    for k in range(1,(target/3)+1):
        seqfrac.extend([1, 2*k, 1])

    num, _ = findfract(2, seqfrac[:target])

    print "RESULT=%d" % (sum([int(c) for c in str(num)]))

