while True:
    strInput = input()
    if strInput == '0 0':
        break

    listInput = strInput.split()

    for i in range(2):
        listInput[i] = int(listInput[i])

    if listInput[0] > listInput[1]:
        if listInput[0] % listInput[1] == 0:
            print('multiple')
        else:
            print('neither')

    else:
        if listInput[1] % listInput[1] == 0:
            print('factor')
        else:
            print('neither')
