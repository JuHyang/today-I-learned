import sys

N = int (sys.stdin.readline())

list_num = []

for i in range (N) :
    list_num.append(int (sys.stdin.readline()))

list_num.sort()

max_num = max (list_num)
min_num = min (list_num)

dict_num = dict ()
for i in range (N) :
    if list_num[i] in dict_num :
        dict_num[list_num[i]] += 1
    else :
        dict_num[list_num[i]] = 1

max_count = max (list (dict_num.values()))
min_count = min (list (dict_num.values()))
if list(dict_num.values()).count(max_count) > 1 :
    status = 1
else :
    status = 0

list_temp = []

for k, v in dict_num.items() :
    if v == max_count :
        if status == 0 :
            max_key = k
            break
        else :
            list_temp.append(k)
if status != 0 :
    max_key = sorted(list_temp)[1]

avg = sum (list_num) / N
avg = int (round (avg, 0))
middle = list_num[int (N / 2)]
mode = max_key
range_num = max_num - min_num


print (avg)
print (middle)
print (mode)
print (range_num)
