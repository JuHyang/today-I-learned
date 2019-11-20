

case = int (input ())

for i in range (case) :
    count = 1
    input_str = input ()
    list_input = input_str.split()
    list_name = []

    N = int (list_input[0])
    M = int (list_input[1])

    input_major = input ()
    list_major = input_major.split()
    for i in range (N) :
        list_major[i] = int (list_major[i])
        list_name.append (i)


    while len (list_major) != 0 :
        max_list = max (list_major)
        if list_major[0] != max_list :
            list_major.append(list_major.pop(0))
            list_name.append(list_name.pop(0))

        else :
            if list_name[0] == M :
                print (count)
                break
            list_major.pop(0)
            list_name.pop(0)
            count += 1
