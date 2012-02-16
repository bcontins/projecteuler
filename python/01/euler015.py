from math import factorial

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    print "RESULT=%d" % (choose(40, 20))


