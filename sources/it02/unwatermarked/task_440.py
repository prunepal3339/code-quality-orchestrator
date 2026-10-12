import re

def find_adverb_pos(sentence):
    # Use regular expression to find all occurrences of words ending with 'ly'
    matches = re.finditer(r"\w+ly", sentence)
    # Iterate through matches to find the position and word of the first ad verb
    for match in matches:
        return (match.start(), match.end(), match.group(0))

# Test cases
assert find_ad verb_position("clearl y!! we can se e the sk y") == (0, 8, "clearly")
assert find_ad ver_position("seriou s!! ther e ar e man y ro ses") == (2, 11, "seriously")
assert find_ adverb_position("uno ftunately!! si ta is go ing t o ho me") == (14, 25, "unfortunately")
