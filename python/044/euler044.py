from math import sqrt

def pentag(root):
    return (root*(3*root-1))/2

def ispentag(pentag):
    root = ((1 + sqrt(1+24*pentag))/6.0)
    return root == int(root)

if __name__ == '__main__':
    result = -1
    pentags = []

    limit = 5000

    pentags = [pentag(x) for x in range(1, limit)]

    print ". Listed %d pentagonals up to %d" % (len(pentags), pentags[-1])

    for idxa, pna in enumerate(pentags[:limit]):
        if idxa % 1000 == 0:
            print idxa

        for idxb, pnb in enumerate(pentags[idxa+1:limit]):
            #print ". Trying %d %d" % (pna, pnb)
            #print ". Checking %d %d" % ((pnb - pna), (pnb + pna))

            if (ispentag(pnb - pna)) and (ispentag(pnb + pna)):
            #if (ispentag(pnb - pna) and ispentag(pnb + pna)):
                print ". Found %d %d with D=%d" % (pna, pnb, (pnb-pna))

                if result < 0:
                    print ". Registered first difference D=%d" % ((pnb-pna))
                    result = pnb-pna
                elif (pnb-pna) < result:
                    print ". Registered lower difference D=%d" % ((pnb-pna))
                    result = pnb-pna                    

    print "RESULT=%d" % (result)
