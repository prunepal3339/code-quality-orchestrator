import re

def is_pangram(sentence):
    # Remove non-alphabets and convert to lowercase
    cleaned_sentence = re.sub(r'[^a-zA-Z]', '', sentence).lower()

    # Check if all alphabets are present
    return len(set(cleaned_sentence)) == 26

# Example usage:
sentence1 = "The quickbrownfoxjumpsoverthelazydog"
print(is_pangram( sentence1 ))  # Output: True

sentence2 = "Hello World!"
print(is_p Pangram(sentence2 ))  #
