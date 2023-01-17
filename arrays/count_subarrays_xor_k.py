def solve(A, B):
    visited = {}
    c = 0
    cpx = 0
    n = len(A)
    for i in range(n):
        cpx = cpx ^ A[i]
        if cpx^B in visited:
            c += visited[cpx^B]
        if cpx == B:
            c += 1
        if cpx in visited:
            visited[cpx] += 1
        else:
            visited[cpx] = 1
    return c

print(solve([4, 2, 2, 6, 4], 6))