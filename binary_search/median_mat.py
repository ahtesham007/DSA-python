def findMedian(mat):
    lo = 1
    hi = 1e9

    
    n,m = len(mat),len(mat[0])

    def lessthatequal(arr,num):
        l = 0
        h = m-1
        while l <= h:
            
            mid = (l+h)//2
            if num >= arr[mid]:
                l = mid + 1
            else:
                h = mid -1
        return l

    while lo<=hi:
        cnt = 0
        mid = (lo+hi)//2
        for i in range(n):
            cnt += lessthatequal(mat[i],mid)

        if cnt <= (n*m)//2:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

print(findMedian([[1, 3, 6],[2, 6, 9],[3, 6, 9]]))