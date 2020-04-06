def solution(jobs):
    jobLength = len(jobs)
    jobs.sort(key=lambda job: (job[0], job[1]))
    print(jobs)
    answer = 0

    nowJob = jobs.pop(0)
    startPoint = nowJob[0]
    endPoint = startPoint + nowJob[1]
    answer += endPoint - nowJob[0]

    while len(jobs) > 0:
        index = -1
        for i in range(len(jobs)):
            if (jobs[i][0] > endPoint):
                break

            if index == -1:
                index = i
            else:
                if (jobs[index][1] > jobs[i][1]):
                    index = i

        if index == -1:
            nowJob = jobs.pop(0)
            startPoint = nowJob[0]
        else:
            nowJob = jobs.pop(index)
            startPoint = endPoint
        endPoint = startPoint + nowJob[1]
        answer += endPoint - nowJob[0]

    return int(answer / jobLength)
