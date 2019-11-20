def solution(s):
    answer = ''
    list_str = s.split()
    list_num = []
    for i in list_str :
        list_num.append(int (i))

    answer += str (min (list_num))
    answer += " " + str(max(list_num))
    return answer