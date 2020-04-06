N = int(input())
meets = []

for i in range(N):
    strInput = input()
    listInput = strInput.split()

    listInput[0] = int(listInput[0])
    listInput[1] = int(listInput[1])
    meets.append(listInput)

meets.sort(key=lambda meet: (meet[1], meet[0]))

count = 1
standard = meets[0]
for meet in meets[1:]:
    if standard[1] > meet[0]:
        continue
    standard = meet
    count += 1

print(count)
