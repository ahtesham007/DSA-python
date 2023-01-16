class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        res = []
        if not nums:
            return res

        nums.sort()

        n = len(nums)
        for i in range(n):
            # Removing duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target2 = target - (nums[i] + nums[j])

                front, back = j + 1, n-1

                while front < back:
                    two_sum = nums[front] + nums[back]
                    if target2 == two_sum:
                        quadruple = [nums[i], nums[j], nums[front], nums[back]]
                        res.append(quadruple)

                        front += 1
                        # Removing duplicates
                        while front < back and nums[front] == nums[front - 1]:
                            front += 1
                        back -= 1
                        while front < back and nums[back] == nums[back+1]:
                            back -= 1
                    
                    elif two_sum < target2:
                        front += 1
                    else:
                        back -= 1

        return res

obj = Solution()
print(obj.fourSum([2,2,2,2,2], 8))