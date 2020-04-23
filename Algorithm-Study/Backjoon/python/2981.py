def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


N = int(input())

numList = []
for i in range(N):
    numList.append(int(input()))

numList.sort()

tempGcd = numList[1] - numList[0]

for i in range(1, N):
    tempGcd = gcd(tempGcd, numList[i] - numList[i - 1])

resultList = []
i = 2
while i ** 2 <= tempGcd:
    if tempGcd % i == 0:
        if i not in resultList:
            resultList.append(i)
        if tempGcd // i not in resultList:
            resultList.append(tempGcd // i)
    i += 1

resultList.sort()
resultList.append(tempGcd)
answer = ""
for num in resultList:
    answer += str(num) + " "


print(answer[:-1])
