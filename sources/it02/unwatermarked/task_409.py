def min_product_tuple(list_of_tuples):
    # Calculate the product of each tuple pair and return the minimum product
    min_product = min([abs(x * y) for x, y in list_of_tuples])
    return min_product
