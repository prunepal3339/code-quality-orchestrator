def find_largest_product(sequence, span):
    max_product = 0
    for i in range(len(sequence) - span + 1):
        product = 1
        for j in range(span):
            product *= int(sequence[i + j])
        max_product = max(max_product, product)
    return max_product

sequence = "63915"
span = 3
print(find_largest_product(sequence, span))