def sortList (listFood, mode) :
    listResult = [listFood[0]]
    for i in range (1, len (listFood)) :
        for j in range (len (listResult)) :
            if listResult[j][mode] > listFood[i][mode] :
                listResult.insert(j, listFood[i])
                break;
            else :
                if j == len (listResult) - 1 :
                    listResult.append(listFood[i])
                    break
                continue
    return listResult

def solution (food_times, k) :
    startIndex = 0
    temp = k
    listFood = []
    for i in range (len (food_times)) :
        listFood.append([i, food_times[i]])

    listFood = sortList (listFood, 1)
    while temp > len (listFood) * listFood[startIndex][1] :
        temp -= len(listFood) * listFood[startIndex][1]
        listFood.pop(0)
        if len (listFood) == 0 :
            return -1

    listFood = sortList (listFood, 0)
    temp = temp % len (listFood)

    return listFood[temp][0] + 1


food_times = [3,1,2]
k = 5

result = solution (food_times, k)
print (result)
