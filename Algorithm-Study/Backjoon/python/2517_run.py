N = int (input ())

human = []
result = []
for i in range (N) :
    human.append(int (input()))


for i in range (N) :
    count = 0
    now = human [i]
    for j in range (i) :
        if human [j] <= now :
            count += 1
    result.append (i - count + 1)

for i in result :
    print (i)