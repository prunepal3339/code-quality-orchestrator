def largest_product(series, span):
    if span > len(series) or span <= 0:
        return None

    max_product = float('-inf')
    current_product = 1
    
    # Iterate through each digit in the series.
    for i in range(len(series)):
        # Multiply the current digit with the current product.
        current_product *= int(series[i])
        
        # If we have reached the span, calculate the maximum product.
        if i >= span - 1:
            # Update the maximum product if the current product is higher.
            max_product = max(max_product, current_product)

            # To get the next series, we need to divide the current product 
            # by the first digit in the previous series.
            current_product /= int(series[i - span + 1])

    return max_product
