class Solution:
    def trap(self, height):
        n = len(height)
        l, r = 0, n-1
        ans = 0
        maxl, maxr = height[l], height[r]

        while l < r:
            if maxl < maxr:
                ans += maxl - height[l]
                l += 1
                maxl = max(maxl, height[l])
            else:
                ans += maxr - height[r]
                r -= 1
                maxr = max(maxr, height[r])
        
        return ans