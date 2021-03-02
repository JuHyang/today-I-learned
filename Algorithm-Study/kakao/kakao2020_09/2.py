from itertools import combinations


def check(order, key):
    for char in key:
        if char not in order:
            return False

    return True


def solution(orders, course):
    answer = []

    for courseNum in course:
        combiList = []
        for order in orders:
            if len(order) < courseNum:
                continue
            combiList += list(combinations(order, courseNum))
        combiSet = set()
        for combi in combiList:
            combiSet.add(''.join(sorted(combi)))

        orderDict = dict()

        maxValue = 0
        for temp in combiSet:
            orderCombi = "".join(list(temp))
            count = 0
            for order in orders:
                if check(order, orderCombi):
                    count += 1
            orderDict[orderCombi] = count
            maxValue = max(maxValue, count)
        if maxValue > 1:
            for key in orderDict.keys():
                if orderDict[key] == maxValue:
                    answer.append(key)
    return sorted(answer)


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
