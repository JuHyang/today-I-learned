from itertools import permutations

str_input = input()

list_input = str_input.split()
N = int(list_input[0])
M = int(list_input[1])
items = []

for i in range(N):
    items.append(str(i + 1))

items = list(map(' '.join, permutations(items, M)))
for item in items:
    print(item)
