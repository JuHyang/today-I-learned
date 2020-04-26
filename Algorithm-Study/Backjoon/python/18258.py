import sys

read = sys.stdin.readline


N = int(read())

queue = []
queueSize = 0
popCount = 0

for i in range(N):
    strInput = read()
    listInput = strInput.split()
    if listInput[0] == 'push':
        queue.append(listInput[1])
        queueSize += 1
    elif listInput[0] == 'pop':
        if queueSize - popCount == 0:
            print(-1)
        else:
            print(queue[popCount])
            popCount += 1
    elif listInput[0] == 'size':
        print(queueSize - popCount)
    elif listInput[0] == 'empty':
        if queueSize - popCount:
            print(0)
        else:
            print(1)
    elif listInput[0] == 'front':
        if queueSize - popCount:
            print(queue[popCount])
        else:
            print(-1)
    elif listInput[0] == 'back':
        if queueSize - popCount:
            print(queue[queueSize - 1])
        else:
            print(-1)
