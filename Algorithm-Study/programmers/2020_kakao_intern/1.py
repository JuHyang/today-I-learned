def distance(number, target) :
    if target == 0 :
        target = 11
    if number == 0 :
        number = 11
    
    if number in [2,5,8,11] :
        return abs(target - number) // 3
    elif number in [1, 4, 7, 10] :
        return abs(target - (number + 1)) // 3 + 1
    else :
        return abs(target - (number - 1)) // 3 + 1

def solution(numbers, hand):
    currentL = 10
    currentR = 12
    answer = ''

    for number in numbers :
        if number == 1 or number == 4 or number == 7 :
            answer += "L"
            currentL = number
        elif number == 3 or number == 6 or number == 9 :
            answer += "R"
            currentR = number
        else :
            distanceL = distance(currentL, number)
            distanceR = distance(currentR, number)
            if distanceL > distanceR :
                answer += "R"
                currentR = number
            elif distanceL < distanceR :
                answer += "L"
                currentL = number
            else :
                if hand == "right":
                    answer += "R"
                    currentR = number
                else :
                    answer += "L"
                    currentL = number
    
    return answer
