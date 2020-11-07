import sys

# Put words into dict as you go and check if they already exist.
def nodup(string):
    wordDict = {}
    spltStr = string.split()

    for word in spltStr:
        if word in wordDict:
            print("no")
            return
        else:
            wordDict[word] = 1
    print("yes")

for line in sys.stdin:
    nodup(line)