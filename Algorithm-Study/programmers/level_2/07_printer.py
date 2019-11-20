def solution(priorities, location):
    temp = []
    for i in range (len (priorities)) :
        temp.append(i)
    answer = 0
    while True :
        if max(priorities) != priorities[0] :
            priorities.append(priorities.pop(0))
            temp.append(temp.pop(0))
        else :
            answer += 1
            priorities.pop(0)
            if temp.pop(0) == location :
                break
    return answer


priorities = [2, 1, 3, 2]
location = 2
print (solution (priorities, location))
