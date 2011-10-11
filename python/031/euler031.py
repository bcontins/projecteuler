coins = [200, 100, 50, 20, 10, 5, 2, 1]

def decomp(val, dec, prev, res):
    result = res

    for cn in [x for x in coins if x <= prev]:
        newval = val - cn
        if newval < 0:
            continue
        elif newval > 0:
            result = decomp(newval, dec+[cn], cn, result)
        else:
            #print ". Found %s" % (str(dec))
            result += 1

    return result

if __name__ == '__main__':
    result = decomp(200, [], 200, 0)
    print "RESULT=%d" % (result)

