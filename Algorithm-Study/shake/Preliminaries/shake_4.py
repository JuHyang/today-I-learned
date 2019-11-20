def check (target, dict_road, i, list_cur, targetIndex) :
    print (list_cur)
    if i not in dict_road :
        return False
    print (target, i, targetIndex)
    if (len (target) == targetIndex) :
        return True
    if target[targetIndex] == list_cur[1] :
        if list_cur[0] in dict_road :
            return check (target, dict_road, list_cur[0], dict_road[list_cur[0]], targetIndex + 1)
            

N = int (input ())

dict_road = dict()
for i in range (N - 1) :
    str_input = input ()
    list_input = str_input.split()
    list_input[0] = int (list_input[0])
    list_input[1] = int (list_input[1])

    if list_input[0] not in dict_road :
        dict_road[list_input[0]] = []
    dict_road[list_input[0]].append (list_input[1:])

target = input ()
result = 0
print (dict_road)
for i in dict_road :
    print ("result : ", result)
    for j in dict_road[i] :
        if check (target, dict_road, i, j, 0) :
            result += 1