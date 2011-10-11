from sympy import Eq, Symbol, solve, ask, Q

def triang(num):
    return (num*(num+1))/2

def pentagroot(val):
    n = Symbol("n")
    res = solve(Eq(3*n**2 - n, val * 2))

    return (res[0] > 0) and res[0] or res[1]

def hexagroot(val):
    n = Symbol("n")
    res = solve(Eq(2*n**2 - n, val))

    return (res[0] > 0) and res[0] or res[1]

if __name__ == '__main__':

    for exp in range(1, 15):
        num = 10**exp
        t = triang(num)

        pr = float(pentagroot(t))
        hr = float(hexagroot(t))

        print ". For %d: pentag root is %f with ratio %f" % (num, pr, (pr/num)*1000000)
        print ". For %d: hexag  root is %f with ratio %f" % (num, hr, (hr/num)*1000000)

