from itertools import permutations

if __name__ == '__main__':
    result = 0

    for num in ["".join(x) for x in permutations("0123456789")]:
        if num[0] == '0':
            continue

        if num[3] not in "02468":
            continue

        if num[5] not in "05":
            continue

        if int(num[1:4]) % 2 != 0:
            continue

        if int(num[2:5]) % 3 != 0:
            continue

        if int(num[3:6]) % 5 != 0:
            continue

        if int(num[4:7]) % 7 != 0:
            continue

        if int(num[5:8]) % 11 != 0:
            continue

        if int(num[6:9]) % 13 != 0:
            continue

        if int(num[7:10]) % 17 != 0:
            continue

        print ". Found %s" % (num)        

        result += int(num)

    print "RESULT=%d" % (result)
