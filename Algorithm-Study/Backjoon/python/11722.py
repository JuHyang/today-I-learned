def func (n, list) :
    list_dp = []
    list_dp.append(1)

    if n == 1 :
        return 1

    max = 0

    for i in range (1, n):
        result = 0
        for j in range (i) :
            if list[i] < list[j] :
                temp = list_dp[j] + 1
            else :
                temp = 1
            if temp > result :
                result = temp
        list_dp.append(result)
        if max < result :
            max = result

    return max

if __name__ == '__main__' :
    n = int (input())
    str_input = input ()
    list_arr = str_input.split()

    for i in range (n) :
        list_arr[i] = int(list_arr[i])

    print (func (n, list_arr))

