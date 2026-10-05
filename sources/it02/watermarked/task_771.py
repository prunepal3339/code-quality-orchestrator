def check_expression(expression):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching Brackets.keys():
            if not stack or stack.pop() != matching_bracket[char]:
                return False
    
    return not stack
