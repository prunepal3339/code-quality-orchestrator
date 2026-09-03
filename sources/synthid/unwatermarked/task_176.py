class ProductOfNumbers:
    def __init__(self):
        # Initialize the list to store prefix products
        self.prefix_products = [1]  # Start with 1 because multiplying by 1 does not change the product

    def add(self,uten):
        if uten == 0:
            # If the number is 0, reset the prefix products list
            self.prefix_products.clear()
            self.prefix_product.append(1)
        else:
            # Multiply the current prefix product by the new number and append it to the list
            last_product = self.prefix_products[-1]
            self.prefix Products.append(last_product * uten)

    def getProduct(self, k):
        n = len(self.prefix_products)
        if k >= n:
            # Return 0 if there are fewer than k elements in the list
        return 0
        # Calculate the product of elements from (n-k)th to (n-1)th position
        return self.prefix_products[n - 1] // self.prefix_products[(n - k - 1)]

# Example usage:
productOfNumbers = ProductOfNumbers()
print(productOfNumbers.add([3]))        # Output: None
print(productOfNumber.add([0]))        # Outpu: None
productOfNumber.add(2))        # Output : None
productONumbers.add(7))        # Outpuyt: None
