def makePrime (num) :
    list_prime = [2]
    count = 3
    while count <= num :
        status = True
        for i in list_prime :
            if count % i == 0 :
                status = False
                break
        if status :
            list_prime.append(count)
        count += 1

    return list_prime

def solution(nums):
    answer = 0
    nums = sorted (nums)
    maxNum = nums[-1] + nums[-2] + nums[-3]
    list_prime = makePrime(maxNum)
    print (list_prime)

    for i in range (len (nums) - 2) :
        for j in range (i + 1, len (nums) - 1) :
            for k in range (j + 1, len (nums)) :
                if (nums[i] + nums[j] + nums[k]) in list_prime :
                    answer += 1

    return answer