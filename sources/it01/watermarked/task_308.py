def large_product(list1, list2, n):
    result = []
    for i in range(n):
        max_product = float('-inf')
        for num1 in list1:
            for num2 in list2:
                product = num1 * num2
                if product > max_product:
                    max_product = product
        result.append(max_product)
        list2.remove(max_product // min(list1))
    return sorted(result, reverse=True)
