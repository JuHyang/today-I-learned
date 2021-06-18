def solution(stones, k): # O(n log n) 풀이
    maxValue = max(stones)
    head = 0
    tail = maxValue
    
    while head <= tail :
        mid = (tail + head) // 2    
        copyStones = stones[:]
        for i in range (len(stones)) :
            copyStones[i] -= mid
            
        count = 0
        status = True

        for stone in copyStones :
            if stone <= 0 :
                count += 1
            else :
                count = 0
                
            if count >= k :
                status = False
                break
        if status == True :
            head = mid + 1
        else :
            tail = mid - 1
    
    return head




def solution(stones, k): ## O(n) 풀이
    maxIndex = 0
    minIndex = 0
    
    array = [[200000001, 0]]
    
    for i in range(len(stones)) :
        # 인덱스가 k 이상 벌어졌을 때 maxIndex += 1

        if stones[i] > array[maxIndex][0]:
            stones[i] = array[maxIndex][0]
            
        while minIndex >= maxIndex :
            if array[minIndex][0] < stones[i] :
                array.pop()
                minIndex -= 1
            elif array[minIndex][0] > stones[i] :
                array.append([stones[i], i + 1])
                minIndex += 1
                break
            else :
                array[minIndex][1] = i + 1
                break
            if minIndex < maxIndex :
                array.append([stones[i], i + 1])
                minIndex += 1

        if i + 1 - array[maxIndex][1] >= k :
            maxIndex += 1
                
    return array[maxIndex][0]