N = int(input())

countTwo = 0
countFive = 0

for i in range(1, N + 1):
    temp = i
    while temp % 2 == 0:
        temp = temp // 2
        countTwo += 1

    while temp % 5 == 0:
        temp = temp // 5
        countFive += 1

print(min(countTwo, countFive))
