N = int (input ())

temp = N

list_num = []

while temp > 0 :
    list_num.append (temp % 10)
    temp = int (temp / 10)

list_num.sort()
list_num.reverse()
print (list_num)
result = ""
for i in range (len (list_num)) :
    result += str(list_num[i])

print (result)
