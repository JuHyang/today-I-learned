input_str = input ()
input_list = input_str.split()

N = int (input_list[0])
M = int (input_list[1])

input_str = input()
input_list = input_str.split()
cards = []
for i in input_list :
    cards.append(int(i))

result = 0

for i in range (N - 2) :
    for j in range (i + 1, N - 1) :
        for k in range (j + 1, N) :
            temp = cards[i] + cards[j] + cards[k] 
            if temp > M :
                continue
            elif temp > result :
                result = temp

print (result)