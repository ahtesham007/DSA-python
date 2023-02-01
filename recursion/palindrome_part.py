def partition(s):
    ans = []
    n = len(s)

    def dfs(ind, path):
        if ind == n:
            ans.append(path.copy())
            return
        
        for i in range(ind, n):
            if isPalindrome(ind, i):
                path.append(s[ind:i+1])
                dfs(i+1, path)
                path.pop()
    
    def isPalindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -=1
        return True
    
    dfs(0, [])
    return ans

print(partition("aabb"))