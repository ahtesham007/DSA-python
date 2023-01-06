def mergeOverlap(intervals:list[list:int]):
    intervals.sort()
    res = []

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    
    return res

# print(mergeOverlap([[1,3],[2,6],[8,10],[15,18]]))
assert mergeOverlap([[1,3], [2,6], [8,10], [15,18]]) == [[1,6], [8,10], [15,18]]
assert mergeOverlap([[1,4], [4,5]]) == [[1,5]]
assert mergeOverlap([[1,4], [0,4]]) == [[0,4]]