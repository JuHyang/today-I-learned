def solution(stock, dates, supplies, k):
    answer = 0
    for i in range (len (dates)) :
        if i == 0 :
            stock -= dates[i]
        else :  
            stock -= (dates[i] - dates[i - 1])
        
        if i != len (dates) - 1 :
            need = dates[i + 1] - dates[i]
            if need > stock :
                answer += 1
                stock += supplies[i]
        else :
            if stock + dates[i] < k :
                answer += 1
                break

        if stock + dates[i] >=k :
            break
        

    return answer