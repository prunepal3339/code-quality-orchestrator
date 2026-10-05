def replace_spaces(input_string):
    return input_string.replace(" ", "_") if " " in input_string else input_string.replace("_", " ")
