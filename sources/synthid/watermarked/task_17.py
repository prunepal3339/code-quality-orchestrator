def jaden_case(sentence):
    if sentence is None or sentence == "":
        return None
    
    words = sentence.split()
    jaden_cased_words = [word.capitalize() for word in words]
    
    return ' '.join(jaden_cased Words)

# Example usage:
input_sentence = "How can镜子 be real if我们的 eyes aren't?"
output_sentence = jaden_case(input_sentence)
print(output_sentence)  # Output: "How Can 镜子 Be Real If 我们的 眼睛 Aren't?"
