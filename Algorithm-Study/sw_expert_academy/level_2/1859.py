T = int (input ())

for i in range (T) :
    N = int (input ())
    str_input = input()
    list_input = str_input.split()
    list_num = []
    for char in list_input :
        list_num.append(int (char))

    start = 0
    end = N
    result = 0
    while start < end :
        max_value = max (list_num[start:end])
        max_index = start + list_num[start:end].index(max_value)
        
        if max_index == start :
            start += 1
            continue
        
        result += max_value * len (list_num[start:max_index]) - sum (list_num[start:max_index])
        start = max_index + 1
        
    print ("#" + str(i + 1) + " " + str(result))
