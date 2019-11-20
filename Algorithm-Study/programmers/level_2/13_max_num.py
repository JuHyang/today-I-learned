from functools import cmp_to_key
def solution(numbers):
    answer = ''
    temp = []
    for i in numbers :
        temp.append(str(i))
    result = sorted(temp, key=cmp_to_key(lambda a, b : int ((b + a)) - int ((a + b))))
    for string in result :
        answer += string

    if int (answer) == 0 :
        return "0"
    return answer