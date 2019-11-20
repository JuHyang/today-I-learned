def merge (list_a, list_b) :
    print ("merge")
    list_result = []
    while len (list_a) != 0 and len(list_b) != 0 :
        print ("count")
        if list_a[0] < list_b[0] :
            list_result.append(list_a[0])
            list_a.pop(0)
        else :
            list_result.append(list_b[0])
            list_b.pop(0)
    if len (list_a) > 0 :
        list_result += list_a
    if len (list_b) > 0 :
        list_result += list_b
    return list_result

def mergeSort (list_input) :
    if len (list_input) == 1 :
        return list_input
    return merge (mergeSort (list_input[:int (len(list_input) / 2)]), mergeSort (list_input[int (len(list_input) / 2):]))

N = int (input ())

list_input = []

for i in range (N) :
    temp = int (input ())
    list_input.append(temp)

list_result = mergeSort(list_input)

for i in list_result :
    print (i)
