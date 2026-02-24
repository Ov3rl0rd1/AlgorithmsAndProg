def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

def is_balanced_recursive(s, stack=None):
    if stack is None:
        stack = []
    
    if not s:
        return len(stack) == 0
    
    char = s[0]
    pairs = {')': '(', ']': '[', '}': '{'}
    
    if char in pairs.values():
        stack.append(char)
    elif char in pairs.keys():
        if not stack or stack[-1] != pairs[char]:
            return False
        stack.pop()
    
    return is_balanced_recursive(s[1:], stack)

print(is_balanced("{}[()](())"))
print(is_balanced("()]()()[]"))