if __name__ == '__main__':
    target = 1001
    size = 1
    val = 1
    result = 1
    
    while size < target:
        size += 2
        for i in range(4):
            val += size - 1
            result += val


    print "RESULT=%d" % (result)

