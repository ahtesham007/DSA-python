class Solution:
    # Brute force Solution
    def longestConsecutiveBf(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        ans = 1
        prev = nums[0]
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                cnt += 1
            elif nums[i] != prev:
                cnt = 1
            
            prev = nums[i]
            ans = max(cnt, ans)
        
        return ans
    
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums:
            return 0

        h_set = set()
        for n in nums:
            h_set.add(n)
        
        longest_streak = 1
        for i in range(len(nums)):
            if nums[i] - 1 not in h_set:
                curr_num = nums[i]
                curr_streak = 1
                while curr_num + 1 in h_set:
                    curr_num += 1
                    curr_streak += 1
        
                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak


obj = Solution()
print(obj.longestConsecutive([1,2,0,1]))