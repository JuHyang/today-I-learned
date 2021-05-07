from itertools import permutations

items = ["*", "-", "+"]
items = list(map(''.join, permutations(items, 3)))

def solution(expression):
    number = ""
    numbers = []
    signal = []
    for char in expression :
        if char != "*" and char != "-" and char != "+" :
            number += char
        else :
            numbers.append(int(number))
            number = ""
            signal.append(char)
    numbers.append(int(number))
    
    answer = 0
    for item in items :
        tempNumbers = numbers[:]
        tempSignals = signal[:]
        for sig in item :
            i = 0
            while i < len(tempSignals) :
                if tempSignals[i] == sig :
                    temp = 0
                    if sig == "*" :
                        temp = tempNumbers[i] * tempNumbers[i + 1]
                    if sig == "+" :
                        temp = tempNumbers[i] + tempNumbers[i + 1]
                    if sig == "-" :
                        temp = tempNumbers[i] - tempNumbers[i + 1]
                    tempSignals.pop(i)
                    tempNumbers[i] = temp
                    tempNumbers.pop(i + 1)
                    continue
                i += 1
        answer = max(abs(tempNumbers[0]), answer)
    return answer