import math

def findMed(nums1, nums2):
    if len(nums1) > len(nums2): findMed(nums2, nums1)
    n1, n2 = len(nums1), len(nums2)

    l,hi = 0, n1 - 1

    while l <= hi:
        cut1 = (l+hi) >> 1
        cut2 = (n1+n2+1)//2 - cut1

        l1 = -math.inf if cut1 == 0 else nums1[cut1-1]
        r1 = math.inf if cut1 == n1 else nums1[cut1]
        l2 = -math.inf if cut2 == 0 else nums2[cut2-1]
        r2 = math.inf if cut2 == n2 else nums2[cut2]

        if l1 <= r2 and l2 <= r1:
            if (n1+n2)%2:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2))/2
        
        elif l1 > r2:
            hi = cut1 - 1
        else:
            l = cut1 + 1
    
    return 0

print(findMed([-5,3,6,12,15], [-12,-10,-6,-3,4,10]))