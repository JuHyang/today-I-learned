def func (n, list) :

    if n == 1:
        return list[0]

    list_dp = [0]

    list_dp.append(list[0])
    list_dp.append(list[0] + list[1])

    for i in range (2, n) :
        temp = max (list[i] + list[i - 1] + list_dp[i - 2], list[i] + list_dp[i - 1])
        temp = max (temp, list_dp[i])

        list_dp.append(temp)

    return list_dp[-1]


if __name__ == '__main__' :
    n = int (input())
    list_input = []
    for i in range (n) :
        temp = int (input ())
        list_input.append(temp)

    print (func (n, list_input))