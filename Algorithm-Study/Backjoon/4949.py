while True:
    strInput = input()

    if strInput == '.':
        break

    stack = []
    for char in strInput:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' :
            if len (stack) == 0 :
                stack.append(0)
                break
            if stack[-1] == '(' :
                stack.pop()
            else :
                break
        elif char == ']' :
            if len (stack) == 0 :
                stack.append(0)
                break
            if stack[-1] == '[' :
                stack.pop()
            else :
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
