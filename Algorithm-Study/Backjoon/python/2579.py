def func (n, list) :
    if n == 1:
        return list[0]
    elif n == 2 :
        return list[0] + list[1]
    elif n == 3:
        return max (list[0] + list[1] , list[0] + list[2])
    list_dp = []
    list_dp.append(list[0])
    list_dp.append(list[0] + list[1])
    list_dp.append (list[0] + list[2])

    result = max (list_dp[1], list_dp[2])
    for i in range (3, n) :
        temp = max (list_dp[i - 2] + list[i], list[i] + list[i-1] + list_dp[i - 3])
        if result < temp :
            result = temp
        list_dp.append(temp)

    return result

if __name__ == "__main__" :
    n = int (input ())
    list_input = []
    for i in range (n) :
        input_int = int (input())
        list_input.append(input_int)
    list_input.reverse()

    print (func (n, list_input))