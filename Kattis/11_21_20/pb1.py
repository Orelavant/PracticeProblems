import sys

def timeSum(input):
    numSolv = 0
    sum = 0
    dict = {}

    for line in input:
        if line == "-1\n":
            break

        info = line.split()
        if info[2] == "wrong":
            if info[1] in dict:
                dict[info[1]] += 20
            else:
                dict[info[1]] = 20
        else:
            numSolv += 1
            sum += int(info[0])
            if info[1] in dict:
                sum += dict[info[1]]

    print(numSolv, sum)

#file = open("acm/2.in")
file = sys.stdin
timeSum(file)
