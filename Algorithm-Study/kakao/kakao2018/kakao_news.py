def getList (string) :
    result = []
    for i in range (len (string) - 1) : 
        if string[i].lower() >= "a" and string[i].lower() <= "z" :
            if string[i + 1].lower() >= "a" and string [i + 1].lower() <= "z" :
                temp = string[i] + string[i+1]
                result.append(temp.lower())

    return result

def solution(str1, str2):
    answer = 0

    list1 = getList(str1)
    list2 = getList(str2)
    result1 = 0
    tempList = list2.copy()
    for i in list1 :
        if i in tempList :
            tempList.pop(tempList.index(i))
            result1 += 1

    result2 = len (list1) + len(list2) - result1
    
    if result2 != 0 :
        answer = result1 / result2
        
    else :
        answer = 1
    answer *= 65536
    answer = int(answer)
    return answer


str1 = "FRANCE"
str2 = "french"

print (solution(str1, str2))
