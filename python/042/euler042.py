from math import sqrt

def istriangle(word):
    val = 2 * sum([(ord(x)-64) for x in word])

    if val == int(sqrt(val)) * (int(sqrt(val)) + 1):
        return True
    else:
        return False

if __name__ == '__main__':
    tabnames = []
    result = 0

    f = open("./042/words.txt", "r")

    for word in f.read().strip().split(","):
        if istriangle(word[1:-1]):
            result += 1

    print "RESULT=%d" % (result)

