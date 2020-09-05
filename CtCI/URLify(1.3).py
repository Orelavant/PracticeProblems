def URLify(string):
    sArr = list(string)

    for i in range(len(sArr)):
        if sArr[i] == " ":
            sArr[i] = "%20"

    return "".join(sArr)