from output.claude.Task176_CLAUDE_claude_3_5_sonnet_20240620 import ProductOfNumbers
from output.codestral.Task176_MISTRAL_codestral_latest import ProductOfNumbers
from output.gemini.Task176_GEMINI_gemini_1_5_pro_001 import ProductOfNumbers
from output.gtp4o.Task176_OPENAI_gpt_4o import ProductOfNumbers
from output.llama3.Task176_PERPLEXITY_llama_3_sonar_large_32k_chat import ProductOfNumbers


productOfNumbers = ProductOfNumbers()

productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
assert productOfNumbers.getProduct(2) == 20  # 5 * 4 = 20

# Test Case 2: Getting product of last 3 numbers
assert productOfNumbers.getProduct(3) == 40  # 2 * 5 * 4 = 40

# Test Case 3: Getting product of last 4 numbers (includes a zero)
assert productOfNumbers.getProduct(4) == 0   # 0 * 2 * 5 * 4 = 0

# Test Case 4: Add a new number after zero and get product
productOfNumbers.add(8)
assert productOfNumbers.getProduct(2) == 32  # 4 * 8 = 32

# Test Case 5: Check product with a larger value of k
productOfNumbers.add(6)
assert productOfNumbers.getProduct(3) == 192  # 8 * 6 * 4 = 192

# Test Case 6: Adding only one number and getting the product
productOfNumbers = ProductOfNumbers()
productOfNumbers.add(5)
assert productOfNumbers.getProduct(1) == 5  # Product of the last 1 number is 5

# Test Case 7: Adding a zero, then checking the product
productOfNumbers.add(0)
assert productOfNumbers.getProduct(1) == 0  # Product of the last 1 number is 0

# Test Case 8: Adding multiple numbers and getting product of last 4

productOfNumbers.add(1)
productOfNumbers.add(2)
productOfNumbers.add(3)
productOfNumbers.add(4)

assert productOfNumbers.getProduct(4) == 24  #  1 * 2 * 3 * 4 = 0

# Test Case 9: Adding a series of numbers without zeros
productOfNumbers = ProductOfNumbers()
productOfNumbers.add(1)
productOfNumbers.add(2)
productOfNumbers.add(3)
productOfNumbers.add(4)
productOfNumbers.add(5)
assert productOfNumbers.getProduct(3) == 60  # 3 * 4 * 5 = 60

# Test Case 10: Adding zero again after some numbers
productOfNumbers.add(0)
assert productOfNumbers.getProduct(2) == 0  # 0 * 4 = 0