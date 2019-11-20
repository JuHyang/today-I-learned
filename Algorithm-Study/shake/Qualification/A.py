def pattern (input_list) :
    list_num = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    
    row_before = -1
    col_before = -1
    for i in range(len (input_list)) :
        input_num = int (input_list[i])
        input_num -= 1

        row = input_num // 3
        col = input_num % 3

        if list_num[row][col] != 0 :
            return False

        if i != 0 :
            if abs(row - row_before) == 2 and abs (col - col_before) == 2 :
                if list_num[1][1] != 1 :
                    return False
            elif abs(row - row_before) == 2 and col == col_before:
                if list_num[1][col] != 1 :
                    return False
            elif abs(col - col_before) == 2 and row == row_before :
                if list_num[row][1] != 1:
                    return False
            elif abs(row - row_before) != 1 and abs(col - col_before) != 1 :
                return False

        list_num[row][col] = 1
        row_before = row
        col_before = col
    return True

L = int (input ())

input_str = input()
input_list = input_str.split()


if pattern(input_list) :
    print ("YES")
else :
    print ("NO")