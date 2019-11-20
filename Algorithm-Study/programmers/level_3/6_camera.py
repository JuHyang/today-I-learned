def isDup (list_a, list_b) :
    if list_a[1] < list_b[0] or list_b[1] < list_a[0] :
        return False
    else :
        return True

def solution(routes):
    routes = sorted(routes)
    answer = 0
    routes2 = []
    routes2.append(routes[0])
    for i in range (1, len(routes)) :
        route = routes[i]

        if (route[0] > route[1]) :
            temp = route[0]
            route[0] = route[1]
            route[1] = temp

        status = True
        for j in range (0, len (routes2)) :
            route2 = routes2[j]
            if isDup(route, route2) :
                route2[0] = max (route2[0], route[0])
                route2[1] = min (route2[1], route[1])
                status = False
                break
        if (status) :
            routes2.append(route)
    answer = len(routes2)
    return answer