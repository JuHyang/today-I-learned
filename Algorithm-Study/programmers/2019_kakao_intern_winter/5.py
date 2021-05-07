# def zeroCount (stones) :
#     zeroValue = 0
#     count = 0
#     index = 0
#     print (stones)
#     while index < len (stones) :
#         if stones[index] == 200000001 :
#             count += 1
#         else :
#             zeroValue = max(zeroValue, count)
#             count = 0
#         index += 1
#     print (zeroValue)
#     input()
#     return zeroValue

# def solution(stones, k):
#     copyStones = stones[:]
#     answer = 0
#     while True :
#         print (copyStones)
#         if zeroCount(copyStones) >= k :
#             break
        
#         minValue = min(copyStones)
#         answer += minValue
#         for i in range (len(copyStones)) :
#             if copyStones[i] == 200000001 : 
#                 continue
#             copyStones[i] -= min(copyStones)
#             if copyStones[i] == 0 :
#                 copyStones[i] = 200000001
#     return answer



def solution(stones, k):
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