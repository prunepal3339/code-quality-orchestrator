# from output.codestral.Task177_MISTRAL_codestral_latest import max_sum_subsequence as max_sum_subsequence
# from output.gtp4o.Task177_OPENAI_gpt_4o import maxSubsequenceSum as max_sum_subsequence
from output.llama3.Task177_PERPLEXITY_llama_3_sonar_large_32k_chat import maxSum as max_sum_subsequence
# Test case 1
assert max_sum_subsequence([10, 2, -10, 5, 20], 2) == 37

# Test case 2
assert max_sum_subsequence([-1, -2, -3], 1) == -1

# Test case 3
assert max_sum_subsequence([10, -2, -10, -5, 20], 2) == 23

# Test case 4
assert max_sum_subsequence([1, 2, 3, 4, 5], 2) == 15  # Sum of all elements

# Test case 5
assert max_sum_subsequence([-1, 0, 1], 2) == 1  # Pick 1

# Test case 6
assert max_sum_subsequence([1, -1, 2, 3, -2], 2) == 6  # [1, 2, 3]

# Test case 7
assert max_sum_subsequence([5, -1, 3, -2, 4, -1], 3) == 12  # [5, 3, 4]

# Test case 8
assert max_sum_subsequence([2, 1, -2, 3, -4], 1) == 6

# Test case 9
assert max_sum_subsequence([10, -2, 3, -4, 5], 4) == 18

# Test case 10
assert max_sum_subsequence([1, -2, 3, 10, -1], 2) == 14

print("All test cases passed!")