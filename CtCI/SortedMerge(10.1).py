def sortedMerge(A, B, lastA, lastB):
    indexB = lastB - 1
    indexA = lastA - 1
    indexAB = lastA + lastB - 1

    while indexB >= 0:
        if B[indexB] >= A[indexA]:
            A[indexAB] = B[indexB]
            indexB -= 1
        else:
            A[indexAB] = A[indexA]
            indexA -= 1
        indexAB -= 1

    return A