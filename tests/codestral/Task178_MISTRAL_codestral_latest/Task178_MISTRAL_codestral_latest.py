from output.codestral.Task178_MISTRAL_codestral_latest import shortest_subarray
# from output.gtp4o.Task178_OPENAI_gpt_4o import shortest_subarray
# from output.llama3.Task178_PERPLEXITY_llama_3_sonar_large_32k_chat import shortest_subarray

# Test case 1
assert shortest_subarray([1], 1) == 1

# Test case 2
assert shortest_subarray([1, 2], 4) == -1

# Test case 3
assert shortest_subarray([2, -1, 2], 3) == 3

# Test case 4
assert shortest_subarray([1, 2, 3, 4, 5], 11) == 3

# Test case 5
assert shortest_subarray([1, 2, 3, 4, 5], 15) == 5

# Test case 6
assert shortest_subarray([10, -5, 10], 10) == 1

# Test case 7
assert shortest_subarray([-1, -1, -1, -1, 5], 5) == 1

# Test case 8
assert shortest_subarray([1, -2, 3, 4, 5], 7) == 2

# Test case 9
assert shortest_subarray([100, -50, 50, 50, 50], 150) == 3

# Test case 10
assert shortest_subarray([5, -10, 7, -2, 15], 15) == 1

print("All test cases passed!")