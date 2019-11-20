def compare(log1, log2):
    if log1[0] < log2[0]:
        return 2
    elif log1[0] > log2[0]:
        return 1
    else:
        if log1[1] < log2[1]:
            return 2
        elif log1[1] > log2[1]:
            return 1
        else:
            if log1[2] < log2[2]:
                return 2
            elif log1[2] > log2[2]:
                return 1
            else:
                return 3


def check(logs, logStart, logEnd):
    result = 0
    logStart = round (logStart ,3)
    logEnd = round (logEnd, 3)
    for log in logs:
        logTempStart = log[0][0] * 3600 + log[0][1] * 60 + log[0][2]
        logTempEnd = log[1][0] * 3600 + log[1][1] * 60 + log[1][2]
        if logStart > logTempEnd:
            continue
        if logEnd < logTempStart:
            continue
        result += 1
    return result


def solution(lines):
    answer = 0
    logs = []
    for line in lines:
        temp = line.split(" ")
        endTimeList = temp[1].split(":")
        endTimeList[0] = int(endTimeList[0])
        endTimeList[1] = int(endTimeList[1])
        endTimeList[2] = float(endTimeList[2])

        startTimeList = endTimeList.copy()
        startTimeList[2] -= float(temp[2][:-1])
        startTimeList[2] += 0.001
        startTimeList[2] = round (startTimeList[2], 3)

        if startTimeList[2] < 0:
            startTimeList[1] -= 1
            startTimeList[2] += 60

        if startTimeList[1] < 0:
            startTimeList[0] -= 1
            startTimeList[1] += 60

        log = [startTimeList, endTimeList]
        logs.append(log)

    for log in logs:
        logStart = log[0][0] * 3600 + log[0][1] * 60 + log[0][2]
        logEnd = log[1][0] * 3600 + log[1][1] * 60 + log[1][2]
        answer = max(answer, check(logs, logStart - 1 + 0.001, logStart))
        answer = max(answer, check(logs, logStart, logStart + 1 - 0.001))
        answer = max(answer, check(logs, logEnd - 1 + 0.001, logEnd))
        answer = max(answer, check(logs, logEnd, logEnd + 1 - 0.001))
    return answer