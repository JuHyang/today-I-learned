def binarySearch(m, low, high, cards):
    if low > high:
        return 0

    else:
        mid = (low + high) // 2

        if cards[mid] > m:
            return binarySearch(m, low, mid - 1, cards)
        elif cards[mid] < m:
            return binarySearch(m, mid + 1, high, cards)
        else:
            return cards[low:high+1].count(m)


N = int(input())

cards = list(map(int, input().split()))
cards = sorted(cards)

dictCards = dict()

M = int(input())

numberList = list(map(int, input().split()))


for num in numberList:
    if num not in dictCards:
        dictCards[num] = binarySearch(num, 0, N - 1, cards)

result = ""
for num in numberList:
    result += str(dictCards[num]) + " "

print(result[:-1])
