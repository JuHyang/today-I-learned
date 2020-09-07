def binarySearch(m, low, high, nNumberList):
    if low > high:
        return False

    else:
        mid = (low + high) // 2

        if nNumberList[mid] > m:
            return binarySearch(m, low, mid - 1, nNumberList)
        elif nNumberList[mid] < m:
            return binarySearch(m, mid + 1, high, nNumberList)
        else:
            return True


N = int(input())

nNumberList = list(map(int, input().split()))

nNumberList = sorted(nNumberList)

M = int(input())

mNumberList = list(map(int, input().split()))

for mNumber in mNumberList:
    if (binarySearch(mNumber, 0, N-1, nNumberList)):
        print(1)
    else:
        print(0)
