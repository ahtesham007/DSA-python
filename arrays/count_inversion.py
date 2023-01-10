def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += mid - i
        k += 1

    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right):
        arr[i] = temp[i]

    return inv_count

def merge_sort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (left + (right-1)) // 2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, left, mid+1, right)
    return inv_count

n = 10
print(merge_sort([52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162], [0]*n, 0, n))