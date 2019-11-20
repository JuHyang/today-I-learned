def sort (N, list_stages) :
    list_result = []
    for i in range (N) :
        max_list = max (list_stages)
        index = list_stages.index(max_list)
        list_stages[index] = -1
        list_result.append(index + 1)
    return list_result

def solution(N, stages):
    list_stages = []
    humans = len (stages)

    for i in range (N) :
        list_stages.append(0)

    for i in stages :
        if i > N :
            continue
        list_stages[i-1] += 1

    for i in range (N) :
        temp = list_stages[i]
        if temp == 0 :
            continue
        list_stages[i] = list_stages[i] / humans
        humans = humans - temp

    answer = sort(N, list_stages)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = solution (N, stages)
print (answer)
