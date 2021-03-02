def check(user, question):
    for i in range(5):
        if question[i] == "-":
            continue

        if i == 4:
            if int(user[i]) >= question[i]:
                return 1
        elif user[i] != question[i]:
            return 0
    return 1


def check2(user, question):
    for i in range(5):
        if question[i] == "-":
            continue

        if i == 4:
            if int(user.split()[-1]) >= question[i]:
                return 1
            else:
                return 0
        elif question[i] not in user:
            return 0
    return 1


def solution(info, query):
    answer = []

    userList = []

    # for temp in info:
    #     userList.append(temp.split())

    for question in query:
        result = list(range(0, len(userList)))

        questionList = question.split()

        lang = questionList[0]
        part = questionList[2]
        exper = questionList[4]
        food = questionList[6]
        score = int(questionList[7])

        temp = [lang, part, exper, food, score]

        count = 0
        for user in info:
            count += check2(user, temp)

        answer.append(count)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
