import collections

# Takes into account whitespace and case sensitivity. O(n).
def checkPermutation(s1, s2):
    s1Counter = collections.Counter(s1)
    s2Counter = collections.Counter(s2)

    result = s1Counter - s2Counter

    if not result:
        return True
    return False

