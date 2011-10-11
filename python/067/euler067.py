triangle = []

depth = 0

if __name__ == '__main__':
    f = open("./067/triangle.txt", "r")

    for line in f.readlines():
        triangle.append([int(x) for x in line.split(' ')])

    depth = len(triangle)

    for row in range(1, depth):
        width = len(triangle[row])
        for col in range(width):
            if col == 0:
                triangle[row][0] += triangle[row-1][0]
            elif col == width - 1:
                triangle[row][-1] += triangle[row-1][-1]
            else:
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])

    print "RESULT=%d" % (max(triangle[-1]))

