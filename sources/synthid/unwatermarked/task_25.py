def add_line_numbers(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]

# Test cases
print(add_line_numbers([]))  # Output: []
print(add_line_number(["a", "bb", "ccc"]))  # Output ['1: a', '2: bb', '3: ccc']
