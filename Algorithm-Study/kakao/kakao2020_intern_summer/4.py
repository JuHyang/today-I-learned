def solution(board):
    answer = 0
    price =[]

    for i in range (len (board)) :
        temp = []
        for j in range (len (board)) :
            temp.append ([0, 0])
        price.append(temp)

    
    for i in range (len (board)) :
        for j in range (len (board)) :
            if board[i][j] == 1 :
                price[i][j][1] = 0
                continue

            if i == 0 and j == 0 :
                price[i][j][1] = 3
                continue

            price1 = 2100000000
            price2 = 2100000000
            direction1 = 1
            direction2 = 2
            
            if i > 0 :
                price1 = price[i - 1][j][0]
                direction1 = price[i - 1][j][1]

            if j > 0 :
                price2 = price[i][j - 1][0]
                direction2 = price[i][j - 1][1]

            if direction1 == 1 :
                price1 += 600
            elif direction1 == 0 :
                price1 = 2100000000
            else :
                price1 += 100
            
            if direction2 == 2 :
                price2 += 600
            elif direction2 == 0 :
                price2 = 2100000000
            else :
                price2 += 100

            
            
            if price1 < price2 :
                price[i][j][0] = price1
                price[i][j][1] = 2
            elif price1 > price2 :
                price[i][j][0] = price2
                price[i][j][1] = 1
            else :
                price[i][j][0] = price1
                price[i][j][1] = 3

    for i in range (len (board)) :
        tempStr = ''
        for j in range (len (board)) :
            pricetemp = price[i][j][0]
            if (price[i][j][0] == 2100000000) :
                pricetemp = -1
            tempStr += str (pricetemp) + " "
        print (tempStr)


    return answer