def solution(cacheSize, cities):
    cache = []
    if cacheSize == 0 :
        return len (cities) * 5
    answer = 0

    for i in cities :
        city = i.lower()
        if city not in cache :
            answer += 5
            if len (cache) == cacheSize :
                cache.pop(0)
            cache.append(city)
        else :
            answer += 1
            index = cache.index(city)
            cache.append (cache.pop(index))
            
    return answer




cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print (solution (cacheSize, cities))
