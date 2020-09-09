def installRouter(value, homes):
    count = 1
    current = homes[0]

    for i in range(1, len(homes)):
        if homes[i] - current >= value:
            count += 1
            current = homes[i]

    return count


N, C = list(map(int, input().split()))

homes = []
for i in range(N):
    homes.append(int(input()))

homes.sort()

low = 1
high = homes[-1] - homes[0]
result = 0
while low <= high:
    mid = (low + high) // 2

    installedRouter = installRouter(mid, homes)

    if installedRouter >= C:
        if mid > result:
            result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
