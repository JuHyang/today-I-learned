N = int(input())
strInput = input()
listInput = strInput.split()

for i in range(N):
    listInput[i] = int(listInput[i])

listInput.sort()

result = 0
temp = 0
for time in listInput:
    temp += time
    result += temp


print(result)
