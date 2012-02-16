def sumdivs(num):
    sumd = 0

    for cand in range(1, int(num/2)+1):
        if num % cand == 0:
            sumd += cand

    return sumd

if __name__ == '__main__':
    tabisam = [False]
    target = 10000
    result = 0

    for num in range (1, target+1):
        tabisam.append(False)

    for num in range (1, target+1):
        sumd = sumdivs(num)
        if num == sumdivs(sumd) and num != sumd:
            print ". Found amicables: %d and %d" % (num, sumd)
            tabisam[num] = True
    
    for num in range (1, target+1):
        if tabisam[num]:
            result += num

    print "RESULT=%d" % (result)

