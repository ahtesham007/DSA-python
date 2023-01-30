def subset_sum(arr, N):
    ans = []

    def calculate(ind, su):
        if ind == N:
            ans.append(su)
            return
        
        calculate(ind + 1, su + arr[ind])
        calculate(ind + 1, su)
    
    calculate(0, 0)

    ans.sort()
    return ans

print(subset_sum([1,2,3], 3))