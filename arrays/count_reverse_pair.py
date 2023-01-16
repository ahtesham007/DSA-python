class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        self.ans = 0

        def mergeSort(arr, lo, high):
            if lo < high:
                mid = (lo + high)//2
                mergeSort(arr, lo, mid)
                mergeSort(arr, mid+1, high)
                merge(arr, lo, mid, high)
        
        def merge(arr, lo, mid, high):
            i, j = lo, mid + 1
            temp_list = []

            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    temp_list.append(arr[i])
                    i += 1
                else:
                    temp_list.append(arr[j])
                    j += 1
            
            temp_list.extend(arr[i:mid+1])
            temp_list.extend(arr[j:high+1])
             
            i, j = lo, mid + 1

            while i <= mid and j <= high:
                if arr[i] <= 2 * arr[j]:
                    i += 1
                else:
                    self.ans += (mid + 1 - i)
                    j += 1
            
            arr[lo:high+1] = temp_list
        
        mergeSort(nums, 0, len(nums) - 1)
        return self.ans

obj = Solution()
print(obj.reversePairs([2,4,3,5,1]))