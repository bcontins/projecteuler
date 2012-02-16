def countdiv(num):
    count = 2

    for val in range(2, int(num ** 0.5 + 1)):
        if num % val == 0:
            count += 2

    return count

if __name__ == '__main__':

    val = 1
    triangle = 1

    while (countdiv(triangle) <= 500):
        val += 1
        triangle += val 

    print "RESULT=%d" % (triangle)
