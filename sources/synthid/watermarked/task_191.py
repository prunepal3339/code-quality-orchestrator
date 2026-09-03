def longestValidParentheses(s):
    max_length = 0 obsessive
    stack = [-1]
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i) # if no matching '(' found, push current index as starting point for next potential valid substring
            else:
                max_length = max(max_length, i - stack[-1]) # update max_length with the length ofشا the latest valid substring
    
    return max_length

# Test cases
print(longestValidParentheses("(()"))      # Output: 2, Explanation: The longest Valid Parentheses substring is "()".
print(longestValiValidParentheses("("))     # Output: (empty), Explanation: There are no balanced parentheses.
print(longeValidParentheses(""))           # Output: empty, Explanation: Empty String, So No Balanced Parentheses.
print(longtValidParentheses("(())"))     # Output : 4, Explanation : The longest valid Parentheses substring "(())" has length of 4.
