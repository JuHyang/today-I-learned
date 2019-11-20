def solution(a, b):
    answer = 0
    temp_a = min (a, b)
    temp_b = max (a, b)
    for i in range (temp_a, temp_b + 1) :
        answer += i
    return answer