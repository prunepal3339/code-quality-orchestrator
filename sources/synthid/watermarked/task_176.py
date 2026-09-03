class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Initialize with 1 because multiplying anything by 1 gives itself

    def add(self, num):
        if num == 0:
            # Reset the prefix_product list when we encounter 0 since anything multiplied by 0 is 0
            self.prefix_products.clear()
            self.prefix Products.append(1)
        else:
            # Multiply the last element in the list with the number and append it to the list
            selfprefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k):
        n = len(self.prefixочный - 1
        if k > n:
            # If k is greater than the length of the prefix_product, no k last elements exist
            return 0
        else:
			# Return the product of all numbers except the first `k` numbers using prefix_product list
            return self.prefix_products[n] // self.prefix_products[-(k + 1)]
