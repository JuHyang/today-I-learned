def solution(baseball):
    answer = 0
    for i in range (123, 988) :
        number = str (i)
        if number[0] == number[1] or number[1] == number[2] or number[0] == number[2] :
            continue
        if '0' in number :
            continue
        flag = True
        for target in baseball :
            temp = str (target[0])
            strike = target[1]
            ball = target[2]
            for i in range (3) :
                if temp[i] == number[i] :
                    strike -= 1
                    continue
                
                if temp[i] in number :
                    ball -= 1
                    continue
            if strike != 0 or ball != 0 :
                flag = False
                break
        if flag :
            answer += 1
    return answer