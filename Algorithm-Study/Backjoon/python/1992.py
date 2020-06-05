def quadTree (tree, x, y, size) :
    start = tree[y][x]
    for i in range (y, y + size) :
        string = ""
        for j in range (x, x + size) :
            string += tree[i][j] + " "

    if size == 1 :
        return tree[y][x]


    status = True

    result = ''

    for i in range (y, y + size) :
        if status == False :
            break
        for j in range (x, x + size) :
            if tree[i][j] != start :
                status = False
                break

    if status == True :
        result += (start)
    else :
        nextSize = size // 2
        result += '('
        result += (quadTree(tree, x, y, nextSize))
        result += (quadTree(tree, x + nextSize, y, nextSize))
        result += (quadTree(tree, x, y + nextSize, nextSize))
        result += (quadTree(tree, x + nextSize, y + nextSize, nextSize))
        result += ')'
        
    return result


N = int (input())

listInput = []
for i in range (N) :
    listInput.append (input())


result = quadTree (listInput, 0, 0, N)

print (result)