## counting sort
import sys
def countingSort (N, list_num) :
    for i in range (10000) :
        list_num.append(0)
    for i in range (N) :
        list_num[int (sys.stdin.readline()) - 1] += 1
    for i in range (len(list_num)) :
        for j in range (list_num[i]) :
            print (i + 1)
N = int (input ())

list_num = list ()

countingSort(N, list_num)
