def myPow(x, n):
    ans = 1

    nc = n

    if nc<0:
        nc *= -1
    
    while nc > 0:
        if nc%2:
            ans = ans * x
            nc -= 1
        else:
            x *= x
            nc //= 2
    
    if n<0:
        ans = 1/ans
    
    return ans

print(myPow(2.00000, -2))