def sumdivs(num):
    sumd = 0

    for cand in range(1, int(num/2)+1):
        if num % cand == 0:
            sumd += cand

    return sumd

if __name__ == '__main__':
    tababun = []
    limit = 28124
#    limit = 25
    result = 0

    for num in range(12, limit):
        if (num % 1000) == 0:
            print ". Treated %d" % (num)

        if num < sumdivs(num):
            tababun.append(num)

    for num in range(1, limit):
        if (num % 1000) == 0:
            print ". Checked %d" % (num)

        notsum = True
    
        for abuna in [x for x in tababun if x < (num-11)]:
            if (num - abuna) in tababun:
                #print ". Found sum abundant: %d" % (num)
                notsum = False
                break

        if notsum:
            result += num

    print "RESULT=%d" % (result)

