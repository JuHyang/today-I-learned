def solution(board):
    dp =[]
    for i in range (len(board)) :
        tempList = []
        for j in range (len(board)) :
            tempList.append([0, 0])
        dp.append(tempList)

    return dp[-1][-1][1]