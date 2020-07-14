def multiArray(A, B):
    result = []
    for i in range(len(A)):
        temp = []
        for j in range(len(B)):
            tempNum = 0
            for k in range(len(B[0])):
                tempNum += int(A[i][k]) * int(B[k][j])
            temp.append(tempNum % 1000)
        result.append(temp)
    return result


def power(A, B):
    if B == 1:
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A)):
                temp.append(int(A[i][j]) % 1000)
            result.append(temp)
        return result
    if B == 2:
        return multiArray(A, A)

    if B % 2 == 0:
        return power(multiArray(A, A), B // 2)
    else:
        return multiArray(A, power(A, B - 1))


listInput = input().split()

N = int(listInput[0])
B = int(listInput[1])

A = []
for i in range(N):
    A.append(input().split())

result = power(A, B)

for i in range(len(result)):
    string = ""
    for j in range(len(result[0])):
        string += str(result[i][j]) + " "
    print(string.rstrip())
