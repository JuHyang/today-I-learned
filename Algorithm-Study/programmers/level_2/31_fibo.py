def solution(n):
    answer = 0
    fibo = [0, 1]
    index = 1
    while (index < n) :
        fibo.append(fibo[index - 1] + fibo[index])
        index += 1

    answer = fibo[n] % 1234567
    return answer