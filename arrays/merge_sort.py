def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)

def merge(left, right):
  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  if i < len(left):
    merged.extend(left[i:])
  if j < len(right):
    merged.extend(right[j:])
  return merged

arr = [5, 2, 7, 3, 1, 8, 4, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [1, 2, 3, 4, 5, 6, 7, 8]
