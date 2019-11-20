def solution(n, costs):
    answer = 0

    sortedCosts = sorted (costs, key = lambda cost : cost[2])

    connected = []

    for i in range (len (sortedCosts)) :
        start = sortedCosts[i][0]
        end = sortedCosts[i][1]
        cost = sortedCosts[i][2]
        if i == 0 :
            temp = []
            temp.append(start)
            temp.append(end)
            answer += cost
            connected.append(temp)
            continue

        statusStart = -1
        statusEnd = -1
        
        for j in range (len (connected)) :
            if start in connected[j] :
                statusStart = j
            if end in connected[j] :
                statusEnd = j
        
        if statusStart == -1 and statusEnd == -1 :
            temp = []
            temp.append(start)
            temp.append(end)
            answer += cost
            connected.append(temp)
        elif statusStart == -1 and statusEnd != -1 :
            connected[statusEnd].append(start)
            answer += cost
        elif statusStart != -1 and statusEnd == -1 :
            connected[statusStart].append(end)
            answer += cost
        elif statusStart != -1 and statusEnd != -1 :
            if statusStart != statusEnd :
                connected[statusStart] += connected[statusEnd]
                connected.pop(statusEnd)
                answer += cost
    return answer