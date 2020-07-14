T = int(input())

for time in range(T):
    clothes = {}
    N = int(input())

    for i in range(N):
        strInput = input()
        listInput = strInput.split()
        if listInput[1] in clothes:
            clothes[listInput[1]] += 1
        else:
            clothes[listInput[1]] = 1
    result = 1
    for count in clothes.values():
        result *= count + 1
    print(result - 1)
