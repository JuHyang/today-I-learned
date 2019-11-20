list_a = []
list_b = []

n = int (input ())
price = input()

list_a = price.split()
for i in range(n) :
    list_a[i] = int (list_a[i])
list_b = list_a.copy()

for k in range (1, n) :
    for j in range (k) :
        list_b[k]= max (list_b[k], list_b[j] + list_b[k - j - 1])

print (list_b[n-1])