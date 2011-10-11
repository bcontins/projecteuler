import time

def decipher(cipher, key):
    cleartext = []
    countvalid=0

    minvalid = ord('A')
    maxvalid = ord('z')

    for idx, letter in enumerate(cipher):
        clearletter = letter ^ key[idx % len(key)]
        cleartext.append(chr(clearletter))
        if (clearletter >= minvalid and clearletter <= maxvalid) or clearletter == ord(' '):
            countvalid += 1

    return float(countvalid)/len(cleartext), "".join(cleartext)

def findkey(cipher):
    keyvals = range(ord('a'), ord('z')+1)
    common = ["and", "the", "is"]

    for ka in keyvals:
        for kb in keyvals:
           for kc in keyvals:

                proba, cleartext = decipher(cipher, (ka, kb, kc))

                if proba > 0.9 and reduce(lambda x, y: x and y, [(word in cleartext) for word in common]):
                    return cleartext

if __name__ == '__main__':
    f = open("./059/cipher1.txt", "r")

    cipher = [int(char) for char in f.read().strip().split(",")]

    cleartext = findkey(cipher)

    print "RESULT=%d" % (sum([ord(char) for char in cleartext]))

