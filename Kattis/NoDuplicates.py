import sys


def nodup(string):
    wordDict = {}

    start = 0
    i = 0
    while i < len(string):
        if string[i] == " ":
            word = string[start:i]
            if inDict(word, wordDict):
                return
            start = i + 1
        elif i == len(string) - 1:
            word = string[start:i + 1]
            if inDict(word, wordDict):
                return
        i += 1

    print("yes")


def inDict(word, wordDict):
    if word in wordDict:
        print("no")
        return True
    else:
        wordDict[word] = 1

# for line in sys.stdin:
#     nodup(line)