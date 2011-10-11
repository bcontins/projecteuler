import math

if __name__ == '__main__':
    result = 0

    for num in range(3, 1000000):
        sumf = sum([math.factorial(int(c)) for c in str(num)])

        if sumf == num:
            print ". Found %d" % num
            result += num

    print "RESULT=%d" % (result)

