

resultList = []

for i in range (21) :
    secondList = []
    for j in range (21) :
        firstList = [-1] * 21
        secondList.append(firstList)
    resultList.append(secondList)

def w(a, b, c) :
    global resultList

    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    
    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    if resultList[a][b][c] != -1 :
        return resultList[a][b][c]

    if a < b and b < c :
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c) 

    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

for i in range (0, 21) :
    for j in range (0, 21) :
        for k in range (0, 21) :
            resultList[i][j][k] = w(i, j, k)

while True :
    a, b, c = list(map(int, input().split()))

    if a == -1 and b == -1 and c == -1 :
        break
    else :
        printString = 'w({a}, {b}, {c}) = {result}'
        print (printString.format(a = a, b = b, c = c, result = w(a, b, c)))