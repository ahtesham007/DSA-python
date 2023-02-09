import math
def kthElement(arr1, arr2, n, m, k):        
        if n > m:
            kthElement(arr2, arr1, m, n, k)
        
        l = max(0, k-m)
        h = min(n,k)
        
        while l<=h:
            cut1 = (l+h) >> 1
            cut2 = k - cut1
            
            l1 = -math.inf if cut1 == 0 else arr1[cut1-1]
            l2 = -math.inf if cut2 == 0 else arr2[cut2-1]
            r1 = math.inf if cut1 == n else arr1[cut1]
            r2 = math.inf if cut2 == m else arr2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            elif l1>r2:
                h = cut1 - 1
            else:
                l = cut1 + 1
        
        return 1
print(kthElement([2, 3, 6, 7, 9],[1, 4, 8, 10], 5, 4, 5))