day = 2

mlen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapmlen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0

if __name__ == '__main__':
    for year in range (1901, 2001):
        for month in range (12):
            #print ". Month %d/%d starts on %d" % (month+1, year, day)

            if day == 0:
                #print ". Month %d/%d starts on sunday" % (month+1, year)
                count += 1

            if year % 4 == 0 and year != 2000:
                #print ". Year %d is leap" % (year)
                day = (day + leapmlen[month]) % 7
            else:
                day = (day + mlen[month]) % 7

    print "RESULT=%d" % (count)

