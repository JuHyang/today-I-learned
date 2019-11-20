def solution(n):
    answer = ''
    temp = str (n)
    list_str = []
    for i in temp :
        list_str.append(i)
    list_str.sort()
    list_str.reverse()
    for i in list_str :
        answer += i
    answer = int (answer)
    return answer