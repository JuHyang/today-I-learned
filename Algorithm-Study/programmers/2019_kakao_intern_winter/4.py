def solution(k, room_number):
    answer = []
    room = dict()
    
    for roomNum in room_number :
        index = roomNum
        tempList = [index]
        
        while index in room :
            index = room[index]
            tempList.append(index)
        
        for temp in tempList :
            if temp not in room :
                room[temp] = 0
            room[temp] = index + 1

        answer.append(index)
            
    return answer