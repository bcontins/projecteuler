if __name__ == '__main__':
    tabnames = []
    result = 0

    f = open("./022/names.txt", "r")

    for name in f.read().strip().split(","):
        tabnames.append(name[1:-1])

    tabnames.sort()

    for idx, name in enumerate(tabnames):
        sumn = 0

        for char in name:
            sumn += ord(char)-64

        result += (idx + 1) * sumn

    print "RESULT=%d" % (result)

