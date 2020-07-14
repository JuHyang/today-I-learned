def find_chess (N, M, chess) :
    temp = chess [N][M]
    result = 0
    for i in range (8) :
        for j in range (8) :
            if i == 0 and j == 0 :
                if temp == 'W' :
                    temp = 'B'
                elif temp == 'B' : 
                    temp = 'W'
                continue
            
            if chess[N + i][M + j] != temp :
                result += 1
            if j != 7 :
                if temp == 'W' :
                    temp = 'B'
                elif temp == 'B' : 
                    temp = 'W'
    return result

str_input = input()
list_input = str_input.split()

N = int (list_input[0])
M = int (list_input[1])

chess = []


for i in range (N) :
    str_input = input ()
    temp = []
    for j in range (M) :
        temp.append(str_input[j])
    chess.append(temp)

N1 = N - 7
M1 = M - 7

result = 65
for i in range (N1) :
    change = 0
    for j in range (M1) :
        change = find_chess(i, j, chess)
        change = min (change, 64 - change)
        result = min (result, change)
    

print (result)