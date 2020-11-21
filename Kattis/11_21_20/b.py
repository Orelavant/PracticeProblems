import sys

def lineUp(file):
    decFlag = True
    incFlag = True
    pArr = []

    for line in file:
        pArr.append(line.rstrip())

    for i in range(2, len(pArr)):
        if pArr[i] <= pArr[i-1]:
            incFlag = False
        elif pArr[i] >= pArr[i-1]:
            decFlag = False
        if not incFlag and not decFlag:
            print("NEITHER")
            return

    if incFlag:
        print("INCREASING")
    else:
        print("DECREASING")

#file = open("lineup/3.in")
file = sys.stdin
lineUp(file)
