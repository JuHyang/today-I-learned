def solution(x, n):
    answer = []
    temp = x
    count = 0
    while count < n :
        answer.append(temp)
        temp += x
        count += 1
    return answer