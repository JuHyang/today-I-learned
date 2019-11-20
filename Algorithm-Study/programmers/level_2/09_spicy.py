def solution(scoville, K):
    import heapq
    data = []
    for s in scoville:
        heapq.heappush(data, s)
    answer = 0
    while len(data) > 0:
        if data[0] >= K:
            return answer
        a = heapq.heappop(data)
        if data != []:
            b = heapq.heappop(data)
            heapq.heappush(data, a + (b * 2))
        answer += 1
    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print (solution (scoville, K))
## heapq 를 몰라서 못품 ..