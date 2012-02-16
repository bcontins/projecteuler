if __name__ == '__main__':
    limit = 1000000
    reach = {"1": False, "89": True}
    result = 0

    for num in range(2, limit):
        steps = []
        step = str(sum([int(digit)**2 for digit in str(num)]))

        while step not in reach:
            steps.append(step)
            step = str(sum([int(digit)**2 for digit in step]))

        reached = reach[step]

        for step in steps:
            reach[step] = reached

        result += reached and 1 or 0

    print "RESULT=%d" % (result)

