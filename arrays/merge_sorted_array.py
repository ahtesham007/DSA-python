def merge_sorted_array(nums1, m, nums2, n):
    # sort without extra space

    i=0
    while i < m and n > 0:
        if nums1[i] > nums2[0]:
            nums1[i], nums2[0] = nums2[0],nums1[i]

            first = nums2[0]
            k = 1
            while k < n and first > nums2[k]:
                nums2[k - 1] = nums2[k]
                k += 1
            nums2[k - 1] = first
        i+=1
        
    return nums1[:m]+nums2[:n]

print(merge_sorted_array([4,5,6,0,0,0], 3, [1,2,3], 3))
assert merge_sorted_array([1, 3, 5], 3, [2, 4, 6], 3) == [1, 2, 3, 4, 5, 6]
assert merge_sorted_array([2, 4, 6], 3, [], 0) == [2, 4, 6]
assert merge_sorted_array([], 0, [2, 4, 6], 3) == [2, 4, 6]
assert merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3) == [1, 2, 2, 3, 5, 6]
# assert merge_sorted_array([5, 3, 1], 3, [6, 4, 2], 3) == [1, 2, 3, 4, 5, 6]