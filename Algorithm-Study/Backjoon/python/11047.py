strInput = input()

listInput = strInput.split()

N = int(listInput[0])
K = int(listInput[1])
money = []
for i in range(N):
    moneyInput = int(input())
    money.insert(0, moneyInput)

result = 0
index = 0
while K != 0:
    if money[index] > K:
        index += 1
        continue
    count = int(K / money[index])
    K -= money[index] * count
    result += count

print(result)
