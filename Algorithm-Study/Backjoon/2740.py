listInput = input().split()

N = int(listInput[0])
M = int(listInput[1])

A = []
for i in range(N):
    A.append(input().split())


B = []

listInput = input().split()

M = int(listInput[0])
K = int(listInput[1])

for i in range(M):
    B.append(input().split())

result = []
for i in range(N):
    temp = []
    for j in range(K):
        tempNum = 0
        for k in range(M):
            tempNum += int(A[i][k]) * int(B[k][j])
        temp.append(tempNum)
    result.append(temp)


for i in range(len(result)):
    string = ""
    for j in range(len(result[0])):
        string += str(result[i][j]) + " "
    print(string.rstrip())
