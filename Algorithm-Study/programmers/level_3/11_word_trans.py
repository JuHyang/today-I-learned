def compare(word, target):
    count = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            count += 1

        if count > 1:
            return count

    return count


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    trackingWord = [begin]
    while len(words) != 0:
        temp = []
        for track in trackingWord:
            for word in words:
                if compare(track, word) == 1:
                    temp.append(word)
                    words.remove(word)
        answer += 1
        if target in temp:
            return answer
        else:
            trackingWord = temp
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
