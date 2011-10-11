def numlen(num):
    small = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num < 20:
        return len(small[num])

    elif num < 100 and num % 10 == 0:
        return len(tens[num/10])

    elif num < 100:
        return len(tens[num/10]) + numlen(num%10)

    elif num < 1000 and num % 100 == 0:
        return numlen(int(num/100)) + len("hundred")

    elif num < 1000:
        return numlen(int(num/100)) + len("hundredand") + numlen(num%100)

    elif num == 1000:
        return len("onethousand")

    else:
        return None

if __name__ == '__main__':
    result = 0
    target = 1000

    for num in xrange(1, target + 1):
        #print ". Length(%d)=%d" % (num, numlen(num))
        result += numlen(num)

    print "RESULT=%d" % (result)

