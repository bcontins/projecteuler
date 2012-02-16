import re

if __name__ == '__main__':
    maxprod = 0

    for num in range(1, 10000):
        product = ""
        mult = 1

        while(len(product) < 9):
            product += str(num * mult)
            mult += 1

        if len(product) > 9:
            continue

        if sorted(product) == list("123456789"):
            print ". Found product %d x %s = %s" % (num, str(range(1, mult)), product)

            if int(product) > maxprod:
                maxprod = int(product)

    print "RESULT=%d" % (maxprod)

