def distance (num1, num2, hand) :
    middle = [2,5,8,11]
    if num1 == num2 :
        return 0

    tempNum1 = num1
    if num1 == 0 :
        tempNum1 = 11
    tempNum2 = num2
    if num2 == 0 :
        tempNum2 = 11
    result = 0

    if hand == "L" :
        if tempNum1 in middle :
            return abs (tempNum1 - tempNum2) // 3
        else :
            tempNum1 += 1
            return abs (tempNum1 - tempNum2) // 3 + 1
    
    else :
        if tempNum1 in middle :
            return abs (tempNum1 - tempNum2) // 3
        else :
            tempNum1 -= 1
            return abs (tempNum1 - tempNum2) // 3 + 1
    return result

def solution(numbers, hand):
    answer = ''

    left = 10
    right = 12
    

    for num in numbers :
        if num == 1 or num == 4 or num == 7 :
            answer += "L"
            left = num
        elif num == 3 or num == 6 or num ==9 :
            answer += "R"
            right = num
        else :
            distanceLeft = distance (left, num, "L")
            distanceRight = distance (right, num, "R")

            if distanceLeft < distanceRight :
                left = num
                answer += "L"
            elif distanceLeft > distanceRight :
                right = num
                answer += "R"
            else :
                if hand == "left" :
                    left = num
                    answer += "L"
                else :
                    right = num
                    answer += "R"

    return answer