#def triang(num):
#    return (num*(num+1))/2
 
def pentag(num):
    return (num*(3*num-1))/2
 
def hexag(num):
    return num*(2*num-1)
 
#triangs = Set([triang(x) for x in range(285,100000)])
pentags = set([hexag(x) for x in range(165,100000)])
hexags = set([pentag(x) for x in range(143,100000)])

common = pentags.intersection(hexags)

print "RESULT=%s" % (",".join([str(x) for x in common]))

