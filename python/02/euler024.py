import math

def findpermut(target, nums):
    print ". Target: %d" % (target)
    print ". Choices: %s" % (str(nums))

    if len(nums) > 1:
        part = (target) / math.factorial(len(nums)-1)
        print ". Part: %d" %(part)

        first = nums[int(target / math.factorial(len(nums)-1))]
        print ". First: %d" %(first)

        nums.remove(first)
        print target % math.factorial(len(nums))
        return "%d%s" % (first, findpermut((target) % math.factorial(len(nums)), nums))
    else:
        print ". Last: %d" %(nums[0])
        return "%d" % nums[0]

if __name__ == '__main__':
    target = 1000000
    nums = range(10)
    result = ""

    result = findpermut(target-1, nums)

    print "RESULT=%s" % (result)

