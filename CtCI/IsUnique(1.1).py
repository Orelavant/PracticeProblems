# Uses an extra data structure. O(n) time.
def isUniqueStructure(string):
    foundDict = {}

    for char in string:
        if char in foundDict:
            return False
        else:
            foundDict[char] = 0

    return True

# No extra data structure. O(n log n) + O(n) if using inplace quicksort.
def isUnique(string):
    sortedString = sorted(string)
    sortedString = "".join(sortedString)

    for i in range(len(sortedString)):
        if sortedString[i+1] == sortedString[i]:
            return False

    return True