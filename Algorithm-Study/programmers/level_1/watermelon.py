def solution(n):
    answer = ''
    str_list = ['수', '박']
    for i in range (n) :
        answer += str_list[i % 2]
    return answer