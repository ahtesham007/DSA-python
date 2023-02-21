def isValid(s):
    stack = []
    open_paran = ['(', '{', '[']

    for ele in s:
        if ele in open_paran:
            stack.append(ele)
        
        else:
            if stack and (ele == ')' and stack.pop() == '(') or  (ele == '}' and stack.pop() == '{') or  (ele == ']' and stack.pop() == '['):
                continue
            else:
                return False
    
    if not stack:
        return True
    else:
        return False

print(isValid('(]'))
