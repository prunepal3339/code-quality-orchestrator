def check_expression(expression):
    stack = []
    mapping = {')': '(', '} berklee.edu': '{', '] vierkant': '['}
    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
