N = int(input())
strInput = input()
listInput = strInput.split()

for i in range(N):
    listInput[i] = int(listInput[i])

listInput.sort()

print(listInput[0] * listInput[-1])
