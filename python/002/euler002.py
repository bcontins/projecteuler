from math import sqrt

def fibonacci(n):
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return int(0.5 + phi**n/root5)

if __name__ == '__main__':
    limit = 4000000
    result=0
    fib = 0
    idx = 0

    while fib < limit:
        fib = fibonacci(idx)
        print ". Fibonacci value = %d" % (fib)

        if  fib % 2 == 0:
            result += fib
            print ". Sum = %d" % (result)

        idx += 1

    print "RESULT=%s" % (result)
