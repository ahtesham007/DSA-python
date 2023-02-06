def findNthRootOfM(n,m):
    def calculate(num):
        res = 1
        for i in range(n):
            res *= num
        return res
    
    lo, high = 1, m

    while (high-lo) > 1e-5:
        mid = (high+lo)/2

        if calculate(mid) > m:
            high = mid
        else:
            lo = mid
    return mid

print(findNthRootOfM(3,27))