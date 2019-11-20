def count_1 (n) :
    count = 0
    while (n > 0) :
        if n % 2 == 1 :
            count += 1
        n = n // 2
    return count

def solution(n):
    answer = 0
    count = count_1 (n)
    temp = n + 1
    while True :
        if count_1 (temp) == count :
            answer = temp
            break
        temp = temp + 1
    return answer