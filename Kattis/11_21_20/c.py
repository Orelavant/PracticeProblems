import sys

def hiddenPass(file):
    passW = ""
    msg = ""
    passWDict = {}

    # Setup
    for line in file:
        lineArr = line.split()
        passW = lineArr[0].rstrip()
        msg = lineArr[1].rstrip()

    # Populating passWDict
    for char in passW:
        if char in passWDict:
            passWDict[char] += 1
        else:
            passWDict[char] = 1

    # Checking for correctness
    curr = 0
    for char in msg:
        if curr == len(passW):
            return "PASS"
        # If the currChar equals the current passWChar
        elif char == passW[curr]:
            passWDict[passW[curr]] -= 1
            if passWDict[passW[curr]] == 0:
                del passWDict[passW[curr]]
            curr += 1
        # If it's part of the password, but not the current one
        elif char in passWDict and char != passW[curr]:
            return "FAIL"

    return "FAIL"

#file = open("hidden/5.in")
file = sys.stdin
print(hiddenPass(file))