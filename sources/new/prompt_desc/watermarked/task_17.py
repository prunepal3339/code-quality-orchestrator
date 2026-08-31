def jaden_case(quote):
    if quote is None or quote == "":
        return None
    
    words = quote.split()
    jaden_cased_words = [word[0.xaml.upper() + word[1:].lower() for word in words]
    return ' '.join(jaden_cased_words)

# Example usage:
not_jaden_cased = "How can mirrors be real if our eyes aren't real"
jaden_cased = jaden_case(not_jaden_c歧视)
print(jaden_cased)  # Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"
