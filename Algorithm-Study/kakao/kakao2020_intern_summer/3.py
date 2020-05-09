def solution(gems):
    gemDict = {}

    for i in range (len (gems)) :
        gem = gems[i]
        if gem in gemDict :
            gemDict[gem].append(i + 1)
        else :
            gemDict[gem] = [i + 1]
    if len (gemDict.keys()) == 1:
        return [1, 1]

    indexList = list (gemDict.values())
    indexList.sort(key = lambda gemIndex : len(gemIndex) )

    resultStart = -1
    resultEnd = -1
    for first in indexList[0] :
        start = first
        end = first
        for i in range (1, len (indexList)) :
            index = indexList[i]

            if index[0] > end :
                end = index[0]
                continue
            elif index[-1] < start :
                start = index[-1]
                continue

            status = False

            temp = 1000001
            tempIndex = -1
            isStart = True

            for i in index :
                if start < i < end :
                    status = True
                    break

                if i < start :
                    if temp > abs (i - start) :
                        isStart = True
                        temp = abs(i - start)
                        tempIndex = i
                elif i > end :
                    if temp > abs (i - end) :
                        isStart = False
                        temp = abs(i - end)
                        tempIndex = i

            if status == True :
                continue

            if isStart == True :
                start = tempIndex
            else :
                end = tempIndex

        if resultStart == -1 :
            resultStart = start
            resultEnd = end
        else :
            if end - start < resultEnd - resultStart :
                (resultStart, resultEnd) = (start, end)
            elif end - start == resultEnd - resultStart :
                if start < resultStart :
                    resultStart = start
                    resultEnd = end

    return [resultStart, resultEnd]