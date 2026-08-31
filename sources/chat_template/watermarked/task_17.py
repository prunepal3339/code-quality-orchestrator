def jaden_case(quote):
    if not quote:
        return None
    return ' '.join(word.capitalize() for word in quote.split())

# Example usage:
print(jaden_case("how can mirrors be real if our eyes aren't real"))
