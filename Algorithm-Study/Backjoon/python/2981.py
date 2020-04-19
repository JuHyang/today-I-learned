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

tempList = []
for i in range(N - 1):
    tempList.append(numList[i + 1] - numList[i])

if len(tempList) == 1:
    tempGCD = tempList[0]
else:
    tempGCD = gcd(tempList[0], tempList[1])
for i in range(2, len(tempList)):
    tempGCD = gcd(tempGCD, tempList[i])

answer = []

for i in range(2, tempGCD // 2):
    if tempGCD % i == 0:
        if i ** 2 == tempGCD:
            answer.append(str(i))
        else:
            answer.append(str(i))
            answer.append(str(tempGCD // i))
answer.append(str(tempGCD))

print(' '.join(answer))
