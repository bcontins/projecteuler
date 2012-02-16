from itertools import permutations

def triang(n):
    return (n*(n+1))/2

def square(n):
    return n**2

def pentag(n):
    return (n*(3*n-1))/2

def hexag(n):
    return n*(2*n-1)

def heptag(n):
    return (n*(5*n-3))/2

def octag(n):
    return n*(3*n-2)

def searchcycle(start, step, order, diccyc):
    if len(order) == 0:
        if start == step:
            return [step,]
        else:
            return None

    try:
        for next in diccyc[order[0]][str(step)[2:]]:
            cycle = searchcycle(start, next, order[1:], diccyc)
            if cycle:
                return [step,] + cycle
    except KeyError:
        return None

    return None

if __name__ == '__main__':

    listtriang = [triang(n) for n in range(1, 141) if triang(n) >= 1000]

    diccyc = {}

    # List all values for a given prefix
    for name, func in (('3', triang), ('4', square), ('5', pentag), ('6', hexag), ('7', heptag), ('8', octag)):
        diccyc[name] = {}

        n = 1
        val = func(1)

        while val < 10000:
            if val >= 1000:
                prefix = str(val)[:2]
                try:
                    diccyc[name][prefix].append(val)
                except KeyError:
                    diccyc[name][prefix] = [val,]

            n += 1
            val = func(n)

    #Parse by starting with triangles and finishing with triangles
    for start in listtriang:
        for order in permutations("45678"):
            #print order
            cycle = searchcycle(start, start, order+('3',), diccyc)
            if cycle:
                break
        if cycle:
            break

    print "RESULT=%d" % (sum(cycle[:-1]))
