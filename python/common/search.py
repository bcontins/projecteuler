def binary_search(value, tab, lower=0, upper=-1):
    if upper < 0:
        upper = len(tab)

    while lower < upper:
        mid = (lower + upper) // 2
        midval = tab[mid]
        if midval < value:
            lower = mid + 1
        elif midval > value:
            upper = mid
        else:
            return mid
    return -1

