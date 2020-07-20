def fibo(n):
    array = [[1, 1], [1, 0]]
    b = [[1, 0]]

    fiboMatrix = multiArray(power(array, n), b)

    return fiboMatrix[1][0]


def multiArray(A, B):
    result = []
    for i in range(len(A)):
        temp = []
        for j in range(len(B[0])):
            tempNum = 0
            for k in range(len(B)):
                tempNum += int(A[i][k]) * int(B[k][j])
            temp.append(tempNum % 1000000)
        result.append(temp)
    return result


def power(A, B):
    if B == 1:
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A)):
                temp.append(int(A[i][j]) % 1000000)
            result.append(temp)
        return result
    if B == 2:
        return multiArray(A, A)

    if B % 2 == 0:
        return power(multiArray(A, A), B // 2)
    else:
        return multiArray(A, power(A, B - 1))


print(fibo(int(input())))
