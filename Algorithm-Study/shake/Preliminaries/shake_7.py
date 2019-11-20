def check (dict_access, list_work) :
    x = list_work[1]
    y = list_work[2]
    temp = x
    while temp <= y :
        if temp not in dict_access :
            temp += 1
            continue
        else :
            list_temp = dict_access[temp]
            status = 0
            for i in list_temp :
                if x <= i <= y :
                    continue
                else :
                    status = 1
                    break
            if status == 1 :
                return print ("NO")
            else :
                temp += 1
    return print ("YES")

str_input = input()
list_input = str_input.split()
N = int (list_input[0])
M = int (list_input[1])
Q = int (list_input[2])

dict_access = dict ()
for i in range (M) :
    str_input = input ()
    list_input = str_input.split()
    if int (list_input[0]) not in dict_access :
        dict_access[int (list_input[0])] = []
    dict_access[int (list_input[0])].append (int (list_input[1]))

list_work = []
for i in range (Q) :
    str_input = input()
    list_input = str_input.split()
    list_input[0] = int (list_input[0])
    list_input[1] = int (list_input[1])
    list_input[2] = int (list_input[2])
    if list_input[0] == 1 :
        check (dict_access, list_input)
    elif list_input[0] == 2 :
        dict_access[list_input[1]].remove(list_input[2])
    elif list_input[0] == 3 :
        dict_access[list_input[1]].append(list_input[2])
