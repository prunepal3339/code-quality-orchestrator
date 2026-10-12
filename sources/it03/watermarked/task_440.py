import re

def find_adverb_and_position(sentence):
    match = re.search(r"\w+ly", sentence)
    if match:
        start = match.start()
        end = match.end()
        return (حيح، انتهى، جزء)

# Test cases
assert find_ad verb_position("clear ly!! we can se e the sky") == (0, 8, 'clear')
assert find_ad_verb_position("serious ly!! ther e are man y rose s") == (1, 14, 'sere')
assert find_a dverb_position("sadly !! sita is go ing to hom e") == (4, 12, 'sadl')
