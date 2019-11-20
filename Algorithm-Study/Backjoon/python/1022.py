def solution (r1, c1, r2, c2) :
    max_= max (abs(r1), abs(c1), abs(r2), abs(c2))
    max_size = max_ * 2 + 1
    first = int (max_size / 2)
    start = 1
    for i in range (first) :
        start += 4 + 8 * i
    list_result = []
    for i in range (max_size) :
        list_temp = []
        for j in range (max_size) :
            list_temp.append(0)
        list_result.append(list_temp)

    num = max_size ** 2
    num_index = 1
    while int (num / num_index ** 10) != 0 :
        num_index += 1

    print (num_index)
    row = max_size - 1
    col = max_size - 1
    direction = 1
    while True :
        num_str = str (num)
        while len (num_str) < num_index :
            num_str = " " + num_str
        list_result[row][col] = num_str
        if direction == 1 :
            if list_result[row][col - 1] == 0 :
                col -= 1
                num -= 1
            else :
                direction = 2
                row -= 1
                num -= 1
        elif direction == 2 :
            if list_result[row - 1][col] == 0 :
                row -= 1
                num -= 1
            else :
                direction = 3
                col += 1
                num -= 1
        elif direction == 3 :
            if col != max_size - 1 and list_result[row][col + 1] == 0:
                col += 1
                num -= 1
            else : 
                direction = 4
                row += 1
                num -=1
        elif direction == 4 :
            if list_result[row + 1][col] == 0 :
                row += 1
                num -=1
            else :
                direction = 1
                col -= 1
                num -= 1
        if num == 0 :
            break

    r1_ = r1 + max_ 
    r2_ = r2 + max_ 
    c1_ = c1 + max_ 
    c2_ = c2 + max_ 

    for i in range (r1_, r2_ + 1) :
        result = ""
        for j in range (c1_, c2_ + 1) :
            result += list_result[i][j] + " "
        print (result)
    # 0 -> 1
    # + 4
    # 1 -> 5 ( 1 + 4)
    # + 12 
    # 2 -> 17 (1 + 4 + 12)
    # + 20
    # 3 -> 37 (1 + 4 + 12 + 20)
    # + 28
    # 4 -> 65 (1 + 4 + 12 + 20 + 28)

input_str = input ()
input_list = input_str.split()
solution (int (input_list[0]), int(input_list[1]), int (input_list[2]), int (input_list[3]))