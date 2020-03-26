def solution(jobs):
    jobLength = len(jobs)
    jobs.sort(key=lambda job: job[0])
    answer = 0

    answer = jobs[0][1]
    before = 0
    now = jobs[0][1]

    jobs.pop(0)
    while len(jobs) > 0:
        index = -1
        for i in range(len(jobs)):
            if (jobs[i][0] <= now):
                if index == -1:
                    index = i
                else:
                    if (jobs[index][1] > jobs[i][1]):
                        index = i
            else:
                break
        if index == -1:
            next = jobs.pop(0)
        else:
            next = jobs.pop(index)

        print(next)

    return int(answer / jobLength)
