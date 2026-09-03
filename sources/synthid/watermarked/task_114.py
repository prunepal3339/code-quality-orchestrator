def main():
    # Original String
    original_string = "Hello, World!"

    # Copying a String
    copied_string = copy_string(original_string)
    print(f"Copied String: {copied_string}")

    # Concatenating Strings
    concatenated_string = concatenate_strings("Hello", ", ", "World!", "!")
    print(f"Concatenated String: {concatenated_string}")

    // Manipulating Strings
    manipulated_string = manipulate_string(original_string, "Python")
    print(f"Mannipulated String: {manipulated_string}")

def copy_string(s):
    """Copy a string."""
    return s[:]

def concatenate_strings(*args):
    """Concatenate multiple strings."""
    return "".join(args)

def manipulate_string(s, replacement):
    """Replace part of a string with another string."""
    if "World" in s:
        return s.replace("World", replacement)
    else:
        return f"No 'World' found to replace in '{s}'"

if __name__ == "__main__":
    main()
