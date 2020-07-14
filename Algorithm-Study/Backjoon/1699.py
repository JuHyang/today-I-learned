def func (n) :
    result = 0
    list_dp = [0, 1, 2, 3]
    list_x = [0, 1]
    x_index = 2
    for i in range (4, n + 1) :
        if x_index ** 2 == i :
            list_x.append(x_index ** 2)
            x_index += 1
            list_dp.append(1)
            continue
        list_dp.append(list_dp[i - 1] + 1)
        for j in list_x :
            list_dp[i] = min (list_dp[i], list_dp[i - j] + 1)
    result = list_dp[-1]
    return result

if __name__ == "__main__" :
    n = int (input ())
    print (func (n))