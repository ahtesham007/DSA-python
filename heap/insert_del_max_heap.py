def heap_insert(arr, n, val):
    arr.append(val)
    i = n
    while i >= 1:
        par = i//2
        if arr[par] < arr[i]:
            arr[par] , arr[i] = arr[i], arr[par]
            i = par
        else:
            return arr
    
    

arr = [10, 5 , 3, 4, 1]

print(heap_insert(arr, 5, 2))
