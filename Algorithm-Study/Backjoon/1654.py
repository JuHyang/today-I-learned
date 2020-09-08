def countNumber(value, lineList):
    if value == 0:
        return
    count = 0

    for line in lineList:
        count += line // value

    return count


numberInput = list(map(int, input().split()))

K = numberInput[0]
N = numberInput[1]

lineList = []
for i in range(K):
    lineList.append(int(input()))

lineList.sort()

low = 1
high = lineList[-1]
result = 0

while low <= high:

    mid = (low + high) // 2

    count = countNumber(mid, lineList)

    if count >= N:
        if mid > result:
            result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
