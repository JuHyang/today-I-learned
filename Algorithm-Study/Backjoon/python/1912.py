def func (n, list) :
    list_dp = []
    list_dp.append(list[0])
    result = list_dp[0]
    for i in range (1, n) :
        temp = max (list[i], list_dp[i - 1] + list[i])
        if result < temp :
            result = temp
        list_dp.append(temp)

    return result

if __name__ == "__main__" :
    n = int (input ())
    list_input_str = input()
    list_input = list_input_str.split()
    for i in range (n) :
        list_input[i] = int (list_input[i])

    print (func(n, list_input))