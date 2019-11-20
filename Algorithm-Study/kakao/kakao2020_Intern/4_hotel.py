def solution(k, room_number):
    answer = []

    room = dict ()

    for roomNum in room_number :
        roomNum = roomNum - 1
        if roomNum not in room :
            room[roomNum] = roomNum + 1
            answer.append(roomNum + 1)

        else :
            temp = []
            temp.append(roomNum)
            nextIndex = room[roomNum]
            while nextIndex in room :
                temp.append(nextIndex)
                nextIndex = room[nextIndex]
            for i in temp :
                room[i] = nextIndex + 1
            room[nextIndex] = nextIndex + 1
            answer.append(nextIndex + 1)

    return answer