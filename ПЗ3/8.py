s = "(()))("

def min_append_detailed(s):
    stack = []
    append_count = 0
    details = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(s):
        if char in pairs.values():
            stack.append((char, i))
        elif char in pairs.keys():
            if stack and stack[-1][0] == pairs[char]:
                stack.pop()
            else:
                details.append((i+append_count, pairs[char]))
                append_count += 1
    
    while stack:
        char, pos = stack.pop()
        append_count += 1
        details.append((pos+append_count, next((k for k, v in pairs.items() if v == char), None) if char in pairs.values() else pairs[char]))
    
    return append_count, details

details = min_append_detailed(s)

print(s)

for pos, char in sorted(details[1], key=lambda x: x[0]):
    s = s[:pos] + char + s[pos:]
    
print(s)