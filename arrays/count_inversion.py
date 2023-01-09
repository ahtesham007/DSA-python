def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += mid - i
        k += 1

    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

def merge_sort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid + 1, right)
    return inv_count

n = 5
print(merge_sort([5,4,3,2,1], [0]*n, 0, n-1))