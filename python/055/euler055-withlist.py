def palin(val):
    return int(str(val)[::-1])

def ispalin(val):
    return val == palin(val)

if __name__ == '__main__':

    result = 0
    limit = 10000
    notlych = []

    for current in range(1, limit):
        islych = True
        num = current
        tested = []

        for iterat in range(50):
            if num in notlych:
                #print ". Number %d already identified as not Lychrel" % current
                islych = False
                notlych.extend(tested)
                break

            elif ispalin(num) and iterat != 0:
                #print ". Number %d reached a palindrome" % current
                islych = False
                notlych.extend(tested)
                break

            else:
                pal = palin(num)
                tested.append(num)
                tested.append(pal)
                num += pal

        if islych:
            #print ". Number %d is a Lychrel" % current
            result += 1

    print "RESULT=%d" % (result)
