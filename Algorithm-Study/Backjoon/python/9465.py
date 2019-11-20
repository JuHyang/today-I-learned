

repeat = int (input ())

for o in range (repeat) :
    list_dp = [[], []]
    list_input = []

    list_temp = []
    n = int (input ())

    for i in range (2) :
        str_input = input ()

        list_str = str_input.split()
        list_temp = []
        for j in range (n) :
            list_temp.append (int(list_str[j]))

        list_input.append(list_temp)

    list_dp[0].append(list_input[0][0])
    list_dp[1].append(list_input[1][0])

    for i in range (1, n) :
        for j in range (2) :
            if j == 0 :
                if i == 1 :
                    temp = list_dp[1][i - 1] + list_input[j][i]
                else :
                    temp = max (list_dp[1][i - 1], list_dp[1][i - 2]) + list_input[j][i]
            elif j == 1:
                if i == 1:
                    temp = list_dp[0][i-1] + list_input[j][i]
                else :
                    temp = max (list_dp[0][i - 1], list_dp[0][i - 2]) + list_input[j][i]

            list_dp[j].append(temp)


    print (max (list_dp[0][-1], list_dp[1][-1]))


