def graphColoring(graph, k, V):
    
    colour = [0]*V
    #your code here
    def solve(node):
        if node == V:
            return True
        
        for i in range(1, k+1):
            if isSafe(i, node):
                colour[node] = i
                if solve(node+1):
                    return True
                colour[node] = 0
        
        return False
    
    def isSafe(col, node):
        for i in range(V):
            if graph[node][i] == 1 and colour[i] == col:
                return False
        return True
    
    if solve(0): return True
    return False
V = 4
m = 3
l = [1, 2, 2, 3, 3, 4, 4 ,1, 1 ,3]
graph = [[0 for i in range(V)] for j in range(V)]
cnt = 0
for i in range(m):
    graph[l[cnt]-1][l[cnt+1]-1]=1
    graph[l[cnt+1]-1][l[cnt]-1]=1
    cnt+=2


print(graphColoring(graph, 3, 4))