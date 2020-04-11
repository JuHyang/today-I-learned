def solution(id_list, k):
    couponDict = {}
    
    for idDay in id_list :
        today = []
        for id in idDay.split() :
            if id not in today :
                today.append (id)

                if id not in couponDict :
                    couponDict[id] = 1
                else :
                    couponDict[id] = min (couponDict[id] + 1, k)

    answer = 0

    for couponCount in couponDict.values() :
        answer += couponCount

    return answer