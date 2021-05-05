import sys

x = int (sys.stdin.readline())

result = list()

result = [-1] * (x + 1)

for i in range (1, len(result)) :
    if i == 1 or i == 2 or i == 3 :
        result[i] = 1
        continue

    result[i] = result[i - 1]
    if i % 2 == 0 :
        result[i] = min (result[i], result[i // 2])
    
    if i % 3 == 0 :
        result[i] = min (result[i], result[i // 3])

    result[i] += 1

if x == 1 :
    print (0)
elif x == 2 or x == 3 :
    print (1)
else :
    print (result[x])