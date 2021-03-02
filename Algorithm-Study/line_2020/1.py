def solution(boxes):
    answer = -1

    countBox = len(boxes)

    numbers = dict()
    for box in boxes:
        for num in box:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

    madeBox = 0

    for num in numbers.keys():
        if numbers[num] >= 2:
            madeBox += numbers[num] // 2

    return countBox - madeBox
