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

        if abs(parentNum) > abs(currentNum) :
            temp = currentNum
            array[index] = parentNum
            array[parentIndex] = temp
        elif abs(parentNum) == abs(currentNum) and parentNum != currentNum :
            array[index] = abs(parentNum)
            array[parentIndex] = -abs(parentNum)
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
        nextValue = -1
        if abs(left) < abs(right) :
            nextIndex = leftIndex
            nextValue = left
        elif abs(left) > abs(right) :
            nextIndex = rightIndex
            nextValue = right
        else :
            if left == right :
                nextIndex = leftIndex
                nextValue = left
            else :
                if left < right :
                    nextIndex = leftIndex
                    nextValue = left
                else :
                    nextIndex = rightIndex
                    nextValue = right

        if abs(currentNum) < abs(nextValue) :
            break
        
        array[index] = nextValue
        array[nextIndex] = currentNum

        if abs(currentNum) == abs(nextValue) and currentNum != nextValue :
            array[index] = -abs(nextValue)
            array[nextIndex] = abs(nextValue)

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


