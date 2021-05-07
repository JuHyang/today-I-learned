def solution(gems):
    gemSet = set(gems)
    
    front = 0
    end = len (gems)
    
    low = 0
    high = 0
    
    gemDict = dict()
    
    while low < len(gems) and high < len(gems) :       
        if len (gemDict) == len (gemSet) :
            if end - front > high - low :
                front = low
                end = high
            gemDict[gems[low]] -= 1
            if gemDict[gems[low]] == 0 :
                del (gemDict[gems[low]])
            low += 1
            continue
            
        if gems[high] not in gemDict :
            gemDict[gems[high]] = 0
        gemDict[gems[high]] += 1
            
        high += 1
            
            
    answer = [front + 1, end]
    return answer


    gems = ["A", "A", "B"];
answer = [2, 3];