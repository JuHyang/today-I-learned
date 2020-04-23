strInput = input()
listInput = strInput.split()
n = int(listInput[0])
m = int(listInput[1])

if m == 0:
    print(0)
else:
    countTwo = 0
    countFive = 0

    i = 2
    while i <= n:
        countTwo += n // i
        i *= 2

    i = 2
    while i <= m:
        countTwo -= m // i
        i *= 2

    i = 2
    while i <= n - m:
        countTwo -= (n - m) // i
        i *= 2

    i = 5
    while i <= n:
        countFive += n // i
        i *= 5

    i = 5
    while i <= m:
        countFive -= m // i
        i *= 5

    i = 5
    while i <= n - m:
        countFive -= (n - m) // i
        i *= 5

    print(min(countTwo, countFive))
