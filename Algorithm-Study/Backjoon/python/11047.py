strInput = input()

listInput = strInput.split()

N = int(listInput[0])
K = int(listInput[1])

money = []
for i in range(N):
    moneyInput = int(input())
    money.append(moneyInput)


result = 0
index = len(money) - 1
while K > 0:
    if money[index] <= K:
        K -= money[index]
        result += 1
    else:
        index -= 1

print(result)
