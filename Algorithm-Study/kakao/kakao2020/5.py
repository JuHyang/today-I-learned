def printBuilding (building) :
    for i in range (1,len (building) + 1) :
        print (building[-i])

def solution(n, build_frame):
    answer = []
    building = []
    for i in range (n + 1) :
        layer = [-1] * (n + 1)
        building.append(layer)

    for target in build_frame :
        x = target[0]
        y = target[1]
        category = target[2]
        action = target[3]
        if action == 1 :
            if category == 0 :
                if y == 0 :
                    building[y][x] = 0
                else :
                    if building[y - 1][x] == 0 or building[y][x - 1] == 1:
                        if building[y][x] == 1 :
                            building[y][x] = 3
                        else :
                            building[y][x] = 0
            else :
                if building[y-1][x] == 0 or building[y - 1][x + 1] == 0 or (building[y][x - 1] == 1 and building[y][x + 1] == 1) :
                    if building[y][x] == 0 :
                        building[y][x] = 3
                    else :
                        building[y][x] = 1
        else :
            if category == 0 :
                

    
    printBuilding(building)
    return answer