def changeBinary (n, num) :
    temp = num
    result = []
    while True:
        if temp == 0 :
            break
        result.insert(0, temp % 2)
        temp /= 2
        temp = int (temp)
    while len (result) < n :
        result.insert (0, 0)
    return result

def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    answer = []
    for i in range (n) :
        map1.append (changeBinary (n, arr1[i]))
        map2.append (changeBinary (n, arr2[i]))
    

    for i in range (n) :
        line = ""
        for j in range (n) :
            if (map1[i][j] + map2[i][j]) != 0 :
                line += "#"
            else :
                line += " "
        answer.append(line)
    
    return answer


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print (solution (n, arr1, arr2))
