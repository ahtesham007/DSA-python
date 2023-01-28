def minimumPlatform(n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        i = 1
        j = 0
        c = 1
        ans = 1
        
        while i < n  and j < n:
            if arr[i] <= dep[j]:
                c += 1
                i += 1
            else:
                c -= 1
                j += 1
            
            ans = max(ans,c)
        
        return ans