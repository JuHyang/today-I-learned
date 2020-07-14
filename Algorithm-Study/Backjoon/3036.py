def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


N = int(input())
strInput = input()
listInput = strInput.split()

first = int(listInput[0])
for i in range(1, N):
    tempGcd = gcd(first, int(listInput[i]))
    print(str(first // tempGcd) + "/" + str(int(listInput[i]) // tempGcd))
