def dup_miss(nums):
    n = len(nums)
    S = (n * (n+1))//2
    SS = (n * (n+1) * (2*n+1))//6

    for num in nums:
        S -= num
        SS -= (num * num)

    miss_num = (S + SS//S)//2

    rep_num = miss_num - S

    return [miss_num, rep_num]

print(dup_miss([4,3,4,1]))