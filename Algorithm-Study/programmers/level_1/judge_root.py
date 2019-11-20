def solution(n):
    answer = 0
    if n ** 0.5 == int (n ** 0.5) :
        temp = int (n ** 0.5)
        answer = (temp + 1) ** 2
    else :
        answer = -1
    return answer