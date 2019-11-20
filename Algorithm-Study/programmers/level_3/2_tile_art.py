def solution(N):
    answer = 0
    before = 1
    after = 1
    for i in range (N - 1) :
        temp = after
        after = before + after
        before = temp
    answer = after * 2 + before * 2
    return answer