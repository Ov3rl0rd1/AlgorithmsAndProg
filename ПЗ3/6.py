def min_deletions(s):
    stack = []
    deletions = 0
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                deletions += 1
    
    deletions += len(stack)
    
    return deletions

print(min_deletions("(()))("))
    