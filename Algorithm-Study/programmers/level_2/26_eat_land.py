def solution(land):
    list_dp = []
    for i in range (len (land)) :
        temp = []
        for j in range (4) :
            if i == 0 :
                temp.append(land[i][j])
            else :
                temp1 = -1
                for k in range (4) :
                    if j == k :
                        continue
                    temp1 = max (temp1, land[i][j] + list_dp[i - 1][k])
                temp.append(temp1)
        list_dp.append(temp)
            
    return max(list_dp[-1])