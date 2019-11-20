def changeToString (num) :
    result = ""
    hour = int (num / 100)
    minute = num % 100
    if minute > 60 :
        minute -= 40

    if hour < 10 :
        result += "0"
    result += str (hour) + ":"

    if minute < 10 :
        result += "0"
    result += str(minute)

    return result

def solution(n, t, m, timetable):
    listTable = []

    busTime = 900
    lastTime = (n - 1) * t
    lastTime = busTime + int (lastTime / 60) * 100 + lastTime % 60
    for i in timetable :
        temp = i.split(":")
        time = int (temp[0]) * 100 + int (temp[1])
        listTable.append(time)
    listTable.sort()

    time = 0
    lastPerson = 0
    while time < n :
        status = 0
        if len (listTable) < m :
            return changeToString(lastTime)
        for i in range (m) :
            if listTable[0] <= busTime :
                lastPerson = listTable.pop(0)
            else :
                status = 1
                break
        if busTime == lastTime :
            if status == 0 :
                return changeToString(lastPerson - 1)
            else :
                return changeToString(lastTime)
        busTime += t
        if busTime % 100 >= 60 :
            busTime += 40
        time += 1

n = 1
t = 1
m = 1
timetable = ["23:59"]
print (solution (n, t, m, timetable))
