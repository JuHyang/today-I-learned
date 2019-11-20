def solution(d, budget):
    answer = 0
    temp = d.copy()
    temp.sort()
    for i in temp :
        budget -= i
        if budget < 0 :
            break
        answer += 1
    return answer