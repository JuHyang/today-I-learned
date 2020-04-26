K = int(input())

inputList = []
for i in range(K):
    inputNum = int(input())
    if (inputNum == 0):
        inputList.pop()
    else:
        inputList.append(inputNum)

print(sum(inputList))
