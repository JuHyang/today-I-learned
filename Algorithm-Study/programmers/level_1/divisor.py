def solution(n):
    answer = 0
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    result_list = []
    for i in range (1, n // 2 + 1) :
        if n % i == 0 :
            if i not in result_list :
                result_list.append(i)
            if n // i not in result_list :
                result_list.append(n // i)
    answer = sum (result_list)
    return answer