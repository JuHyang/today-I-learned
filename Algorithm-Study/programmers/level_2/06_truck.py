def solution(bridge_length, weight, truck_weights):
    answer = 0
    doing = []
    doingTime = []
    todo = truck_weights
    while True :
        answer += 1
        if len (doing) == 0 and len (todo) == 0 :
            break

        if len (todo) > 0 and sum(doing) + todo[0] <= weight :
            doing.append(todo.pop(0))
            doingTime.append(0)
        
        for i in range(len (doingTime)) :
            doingTime[i] += 1
        if len (doingTime) > 0 and doingTime[0] == bridge_length :
            doing.pop(0)
            doingTime.pop(0)
        
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print (solution (bridge_length, weight, truck_weights))
