#  same as n-meeting-room

start = [1,5,10]
end = [4,10,15]

def activity_selection(start, end, n):
    limit = end[0]
    met = 1
    for i in range(1, n):
        if start[i] > limit:
            met += 1
            limit = end[i]
    return met

print(activity_selection(start, end, 3))