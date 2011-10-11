from itertools import permutations
import re
import time

if __name__ == '__main__':
    f = open("./079/keylog.txt", "r")

    logins = []
    digits = []

    for line in [ll.strip() for ll in f.readlines()]:
        logins.append(line)
        digits.extend([char for char in line])

    logins = sorted(list(set(logins)))
    digits = sorted(list(set(digits)))

    for password in ["".join(pp) for pp in permutations(digits)]:
        found = True

        for pattern in [".*".join(list(login)) for login in logins]:

            if not re.search(pattern, password):
                found = False
                break

        if found:
            break

    print "RESULT=%s" % (password)

