def calHeight(value, trees):
    result = 0
    for tree in trees:
        if value >= tree:
            continue
        result += tree - value

    return result


numberInput = list(map(int, input().split()))

N = numberInput[0]
M = numberInput[1]

trees = list(map(int, input().split()))

low = 1
high = max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2

    treeHeight = calHeight(mid, trees)

    if treeHeight >= M:
        if result < mid:
            result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
