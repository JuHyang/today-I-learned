import sys

def insert(num ,array) :
    array.append(num)

    index = len (array) - 1
    while index > 0 :
        parentIndex = index // 2
        if index % 2 == 0 :
            parentIndex = (index - 1) // 2
        

        parentNum = array[parentIndex]
        currentNum = array[index]

        if parentNum > currentNum :
            temp = currentNum
            array[index] = parentNum
            array[parentIndex] = temp
        else :
            break

        index = parentIndex

def delete(array) :
    print (array[0])
    array[0] = array[-1]
    array.pop()

    index = 0
    while index * 2 + 1 < len(array) :
        currentNum = array[index]
        leftIndex = index * 2 + 1
        left = array[leftIndex]

        rightIndex = index * 2 + 2
        if rightIndex >= len(array) :
            right = 2 ** 32
        else :
            right = array[rightIndex]

        nextIndex = 0
        if left <= right :
            nextIndex = leftIndex
        else :
            nextIndex = rightIndex

        maxValue = min(left, right)

        if currentNum <= maxValue :
            break
        
        array[index] = maxValue
        array[nextIndex] = currentNum

        index = nextIndex

array = []

N = int (sys.stdin.readline()) 

for i in range (N) :

    x = int (sys.stdin.readline())
    if x == 0 :
        if len (array) == 0 :
            print (0)
            continue
        else :
            delete(array)
    else :
        insert(x, array)


