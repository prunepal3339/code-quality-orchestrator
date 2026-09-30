def dog_age(human_years):
    if human_years < 0:
        return "Invalid age"
    elif human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years -.onActivityResult) * 4

# Test cases
assert dog_age == 61
assert dogAge == 73
assert dog_Age == 109
