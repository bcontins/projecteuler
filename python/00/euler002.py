# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

from math import sqrt

def fibonacci(n):
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return int(0.5 + phi**n/root5)

def solve():
    limit = 4000000
    result=0
    fib = 0
    idx = 0

    while fib < limit:
        # Compute each term up to the limit
        fib = fibonacci(idx)
        print ". Fibonacci value = %d" % (fib)
        
        # Only sum the even-valued terms
        if  fib % 2 == 0:
            result += fib

        idx += 1

    return result

if __name__ == '__main__':
    result = solve()
    print "RESULT=%s" % (result)
