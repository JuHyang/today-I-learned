def solution(x):
    answer = True
    x_temp = x
    result = 0
    while x_temp != 0 :
        result += x_temp % 10
        x_temp = x_temp // 10
    answer = x % result == 0
    return answer