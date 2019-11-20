def solution(progresses, speeds):
    answer = []
    for i in range (len (progresses)) :
        progresses[i] = 100 - progresses[i]
        progresses[i] = int(progresses[i] / speeds[i])
    
    count = 1
    temp = progresses[0]
    for i in range (1, len (progresses)) :
        
        if temp >= progresses[i] :
            count += 1
        else :
            answer.append(count)
            temp = progresses[i]
            count = 1

        if i == len(progresses) - 1:
            answer.append(count)
            break
    
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print (solution (progresses, speeds))
