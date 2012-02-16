from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r)*factorial(n-r))

if __name__ == '__main__':

    result = 0

    for n in range(1, 101):
        for r in range(1, n):
            if choose(n, r) > 1000000:
                result += 1

    print "RESULT=%d" % (result)
