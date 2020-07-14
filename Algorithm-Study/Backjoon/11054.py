def func (n, list_input) :
    list_dp_1 = []
    list_dp_2 = []
    list_dp_1.append(1)
    list_dp_2.append(1)
    list_re = list (reversed (list_input))

    if n == 1 :
        return 1

    max = 0

    for i in range (1, n):
        result_1 = 0
        result_2 = 0
        for j in range (i) :
            if list_input[i] > list_input[j] :
                temp_1 = list_dp_1[j] + 1
            else :
                temp_1 = 1
            if list_re[i] > list_re[j] :
                temp_2 = list_dp_2[j] + 1
            else :
                temp_2 = 1
            if temp_1 > result_1 :
                result_1 = temp_1
            if temp_2 > result_2 :
                result_2 = temp_2
        list_dp_1.append(result_1)
        list_dp_2.append(result_2)
    max = 0

    for i in range (n) :
        list_dp_1[i] = list_dp_1[i] + list_dp_2[-i - 1] - 1
        if list_dp_1[i] > max :
            max = list_dp_1[i]

    return max

if __name__ == '__main__' :
    n = int (input())
    str_input = input ()
    list_arr = str_input.split()

    for i in range (n) :
        list_arr[i] = int(list_arr[i])

    print (func (n, list_arr))

