strInput = input()
listInput = strInput.split('-')

result = 0

firstNumber = listInput[0]
firstNumberList = firstNumber.split("+")

for num in firstNumberList:
    result += int(num)

for i in range(1, len(listInput)):
    numberList = listInput[i].split('+')
    for num in numberList:
        result -= int(num)


print(result)
