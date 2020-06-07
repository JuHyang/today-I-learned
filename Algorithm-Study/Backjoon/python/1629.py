def customPow (a, n, c) :
    if n == 0 :
        return 1

    temp = customPow (a, n // 2, c)
    if (n % 2 == 0) :
        return temp * temp % c
    else :
        return temp * temp * a % c

listInput = input().split()

for i in range (len(listInput)) :
    listInput[i] = int (listInput[i])

print (customPow(listInput[0], listInput[1], listInput[2]) )