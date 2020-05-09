import itertools

def cal (nums, signInput, signs) :
    numsTemp = nums[:]
    signInputTemp = signInput[:]
    for sign in signs :
        index = 0
        while index < len (signInputTemp) :
            if signInputTemp[index] == sign :
                if sign == '+' :
                    numsTemp[index] = numsTemp[index] + numsTemp[index + 1]
                    numsTemp.pop(index + 1)
                elif sign == '-' :
                    numsTemp[index] = numsTemp[index] - numsTemp[index + 1]
                    numsTemp.pop(index + 1)
                elif sign == '*' :
                    numsTemp[index] = numsTemp[index] * numsTemp[index + 1]
                    numsTemp.pop(index + 1)
                signInputTemp.pop(index)
            else :
                index += 1
    return abs (numsTemp[0])


def solution(expression):
    signs = ['+', '-', '*']
    answer = 0 

    nums = []
    signInput = []
    num = ''

    for i in range (len (expression)) :
        if expression[i] not in signs :
            num += expression[i]
        else :
            nums.append (int (num))
            num = ''
            signInput.append(expression[i])

        if i == len (expression) - 1 :
            nums.append (int (num))

    for sign in list(map(''.join, itertools.permutations(signs))) :
        answer = max (answer, cal (nums, signInput, sign))
    

    return answer