T = int (input ())
for i in range (T) :
    list_fly = []
    str_input = input ()
    list_input = str_input.split()
    N = int (list_input[0])
    M = int (list_input[1])

    for j in range (N) :
        temp = []
        str_input = input()
        list_input = str_input.split()
        for char in list_input :
            temp.append(int(char))
        list_fly.append(temp)
        
    max = 0
    for j in range (N - M + 1) :
        for k in range (N - M + 1) :
            temp = 0
            for o in range (j, j + M) :
                for p in range (k, k + M) :
                    temp += list_fly[o][p]
            if max < temp :
                max = temp
    
    print ("#"+ str(i + 1) + " " + str (max))