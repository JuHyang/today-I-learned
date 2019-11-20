def solution(n):
    answer = 0
    if n == 1 :
        return 1
    if n == 2 :
        return 2

    fibo = [1, 1, 2]
    before = 1
    after = 2
    for i in range (3, n + 1) :
        temp = after
        after = after + before
        before = temp
    answer = after % 1000000007
    return answer