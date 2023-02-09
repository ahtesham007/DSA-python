def agg_cows(stalls, n, c):
    stalls.sort()
    l = 1
    h = stalls[n-1] - stalls[0]
    res = 0

    def is_possible(mid):
        cnt = 1
        placed_cow = stalls[0]
        for i in range(1, n):
            if stalls[i] - placed_cow >= mid:
                cnt+=1
                placed_cow = stalls[i]
        
        if cnt >= c:
            return True
        else:
            return False


    while l <= h:
        mid = (l + h) >> 1

        if is_possible(mid):
            res = mid
            l = mid + 1
        else:
            h = mid - 1
    
    return res

print(agg_cows([1,2,8,4,9], 5, 3))