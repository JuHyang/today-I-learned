class Time :
    def __init__ (self, log, second) :
        logSplit = log.split(":")
        self.hour = int (logSplit[0])
        self.minute = int (logSplit[1])
        self.second = int (float (logSplit[2]) * 1000 - float (second[:-1]) * 1000)

        if self.second < 0 :
            self.second += 6000
            self.minute -= 1
        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1

    def printTime (self) :
        print ("%2d:%2d:%5d"%(self.hour, self.minute, self.second))

def checkTime (log) :
    for i in range (len (log)) :
        

def solution(lines):
    log = []
    for i in lines :
        log.append(i.split()[1:])
    logTime = []
    for i in log :
        startTime = Time (i[0], i[1])
        endTime = Time (i[0], "0s")
        temp = [startTime, endTime]
        logTime.append(temp)

    for i in logTime :
        print("start : %2d:%2d:%5d" %
              (i[0].hour, i[0].minute, i[0].second))
        print("end   : %2d:%2d:%5d" %
              (i[1].hour, i[1].minute, i[1].second))
    
    answer = checkTime (logTime)
    return answer


lines =["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print (solution (lines))
