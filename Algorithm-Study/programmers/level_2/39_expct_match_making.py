def solution(n,a,b):
    answer = 0

    if a > b:
        temp = a
        a = b
        b = temp

    while 2 ** answer < n :
        answer += 1
        if a + 1 == b and a % 2 == 1 :
            break
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2

    return answer