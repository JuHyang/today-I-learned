# import sys

# def maxPush(num, array) :
#     array.append(num)

#     currentIndex = len(array) - 1
#     while currentIndex > 0 :
#         parentIndex = 0
#         if currentIndex % 2 == 0 :
#             parentIndex = (currentIndex - 1) // 2
#         else :
#             parentIndex = currentIndex // 2
        
#         parentValue = array[parentIndex]
#         currentValue = array[currentIndex]

#         if parentValue >= currentValue :
#             break

#         array[currentIndex] = parentValue
#         array[parentIndex] = currentValue

#         currentIndex = parentIndex


# def minPush(num, array) :
#     array.append(num)

#     currentIndex = len(array) - 1
#     while currentIndex > 0 :
#         parentIndex = 0
#         if currentIndex % 2 == 0 :
#             parentIndex = (currentIndex - 1) // 2
#         else :
#             parentIndex = currentIndex // 2
        
#         parentValue = array[parentIndex]
#         currentValue = array[currentIndex]

#         if parentValue <= currentValue :
#             break

#         array[currentIndex] = parentValue
#         array[parentIndex] = currentValue

#         currentIndex = parentIndex

# def maxPop(array) :
#     result = array[0]
#     array[0] = array[-1]
#     array.pop()

#     currentIndex = 0

#     while currentIndex * 2 + 1 < len(array) :
#         currentValue = array[currentIndex]

#         leftIndex = currentIndex * 2 + 1
#         leftValue = array[leftIndex]
        
#         rightIndex = leftIndex + 1
#         rightValue = -10001
#         if rightIndex < len(array) :
#             rightValue = array[rightIndex]

#         nextValue = 0
#         nextIndex = 0

#         if leftValue >= rightValue :
#             nextValue = leftValue
#             nextIndex = leftIndex
#         else :
#             nextValue = rightValue
#             nextIndex = rightIndex

#         if currentValue > nextValue :
#             break

#         array[currentIndex] = nextValue
#         array[nextIndex] = currentValue

#         currentIndex = nextIndex
    
#     return result

# def minPop(array) :
#     result = array[0]
#     array[0] = array[-1]
#     array.pop()

#     currentIndex = 0

#     while currentIndex * 2 + 1 < len(array) :
#         currentValue = array[currentIndex]

#         leftIndex = currentIndex * 2 + 1
#         leftValue = array[leftIndex]
        
#         rightIndex = leftIndex + 1
#         rightValue = 10001
#         if rightIndex < len(array) :
#             rightValue = array[rightIndex]

#         nextValue = 0
#         nextIndex = 0

#         if leftValue <= rightValue :
#             nextValue = leftValue
#             nextIndex = leftIndex
#         else :
#             nextValue = rightValue
#             nextIndex = rightIndex

#         if currentValue < nextValue :
#             break

#         array[currentIndex] = nextValue
#         array[nextIndex] = currentValue

#         currentIndex = nextIndex
    
#     return result


# N = int (sys.stdin.readline())

# maxHeap = []
# minHeap = []

# for i in range (N) :
#     x = int (sys.stdin.readline())

#     if len (maxHeap) == len(minHeap) :
#         maxPush(x, maxHeap)
#     else :
#         minPush(x, minHeap)

#     if len (minHeap) > 0 :
#         if maxHeap[0] > minHeap[0] :
#             maxValue = maxPop(maxHeap)
#             minValue = minPop(minHeap)

#             maxPush(minValue, maxHeap)
#             minPush(maxValue, minHeap)

#     print (maxHeap[0])


import sys
import heapq

N = int(sys.stdin.readline())
left_heap = []
right_heap = []
mid_list = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap,(-number,number))
    else:
        heapq.heappush(right_heap,(number,number))
    if len(left_heap) != 0 and len(right_heap) != 0 and left_heap[0][1] > right_heap[0][1]:
            left_number = heapq.heappop(left_heap)[1]
            right_number = heapq.heappop(right_heap)[1]
            heapq.heappush(left_heap,(-right_number,right_number))
            heapq.heappush(right_heap, (left_number, left_number))
    mid_list.append(left_heap[0][1])

for mid in mid_list:
    sys.stdout.write(str(mid)+"\n")