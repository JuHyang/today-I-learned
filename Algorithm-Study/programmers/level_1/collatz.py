def solution(num):
    answer = 0
    count = 0
    status = True
    if num == 1 :
        return 0
    while count < 500 :
        count += 1
        if num % 2 == 0 :
            num = num // 2
        else :
            num = num * 3 + 1
        
        if num == 1 :
            status = False
            break
    
    if status :
        answer = -1
    else :
        answer = count
    return answer