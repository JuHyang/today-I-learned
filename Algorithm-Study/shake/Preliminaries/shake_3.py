def checkModok (list_life1, list_life2) :
    list_life1.sort()
    list_life2.sort()
    while len (list_life1) != 0 and list_life1[0] <= 0 :
        list_life1.pop(0)
        if len (list_life1) == 0 :
            break
    while list_life2[0] <= 0 :
        list_life2.pop(0)
        if len (list_life2) == 0 :
            return 2
    list_life = list_life1.copy() + list_life2.copy()
    list_life.sort()
    while list_life[0] <= 0 :
        list_life.pop(0)
        if len (list_life) == 0 :
            return 2
    temp = 1
    while len (list_life) != 0 :
        if temp in list_life :
            while temp in list_life :
                list_life.remove(temp)
            temp += 1
        else :
            return 0
    return 1

str_input = input ()
list_input = str_input.split()
N = int (list_input[0])
M = int (list_input[1]) 

list_life_N = []
list_N = []
for i in range (N) :
    str_input = input ()
    list_input = str_input.split()
    for j in range (2) :
        list_input[j] = int (list_input[j])
    list_N.append (list_input)
    list_life_N.append (list_input[1])
list_life_M = []
list_M = []
for i in range (M) :
    str_input = input ()
    list_input = str_input.split()
    for j in range (2) :
        list_input[j] = int (list_input[j])
    list_M.append (list_input)
    list_life_M.append (list_input[1])

if N == 0 and M == 0 :
    print (0)
elif N == 1 and M == 0 :
    print (0)
elif (checkModok (list_life_N, list_life_M)) :
    print ("use modok")
else :
    status = 0
    for i in range (len (list_N)) :
        for j in range (M) :
            list_life1 = list_life_N.copy()
            list_life2 = list_life_M.copy()
            list_life1[i] -= list_M[j][0]
            list_life2[j] -= list_N[i][0]
            check = checkModok (list_life1.copy(), list_life2.copy()) 
            if check == 1 :
                print ("attack", i + 1, j + 1)
                print ("use modok")
                status = 1
                break
            elif check == 2 :
                print ("attack", i + 1, j + 1)
                status = 1
                break
    if status == 0 :
        print (-1)