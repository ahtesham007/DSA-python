def getPermutation(n, k):
    ans = ''
    fact = 1
    nums = []

    for i in range(1, n):
        fact *= i
        nums.append(i)
    nums.append(n)
    k -= 1

    while True:
        ans += str(nums[k//fact])
        nums.pop(k//fact)
        if not nums:
            break

        k %= fact
        fact //= len(nums)
    
    return ans

print(getPermutation(4, 24))
        

