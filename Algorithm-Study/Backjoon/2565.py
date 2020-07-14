N = int (input ())
line = []
for i in range (N) :
    str_input = input()
    list_input = str_input.split()

    temp = []
    temp.append(int (list_input[0]))
    temp.append(int (list_input[1]))

    line.append(temp)

line.sort(key=lambda i : i[0])
temp = []
for i in line :
    temp.append(i[1])

dp = [1] * len (temp)

for i in range (len (temp)) :
    for j in range (i) :
        if temp[i] > temp[j] :
            dp[i] = max (dp[i], dp[j] + 1)
        else :
            dp[i] = max (dp[i], 1)

print (N - max(dp))