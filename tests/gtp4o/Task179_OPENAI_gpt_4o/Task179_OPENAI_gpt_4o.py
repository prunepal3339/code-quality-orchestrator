# from output.codestral.Task179_MISTRAL_codestral_latest import max_sliding_window
# from output.gemini.Task179_GEMINI_gemini_1_5_pro_001 import maxSlidingWindow as max_sliding_window
from output.gtp4o.Task179_OPENAI_gpt_4o import maxSlidingWindow as  max_sliding_window
# from output.llama3.Task179_PERPLEXITY_llama_3_sonar_large_32k_chat import maxSlidingWindow as max_sliding_window

# Test case 1
assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

# Test case 2
assert max_sliding_window([1], 1) == [1]

# Test case 3
assert max_sliding_window([1,-1], 1) == [1, -1]

# Test case 4
assert max_sliding_window([9,11], 2) == [11]

# Test case 5
assert max_sliding_window([4,-2], 2) == [4]

# Test case 6
assert max_sliding_window([7,2,4], 2) == [7, 4]

# Test case 7
assert max_sliding_window([1,3,1,2,0,5], 3) == [3,3,2,5]

# Test case 8
assert max_sliding_window([1,2,3,4,5,6,7,8,9], 3) == [3,4,5,6,7,8,9]

# Test case 9
assert max_sliding_window([10,9,8,7,6,5,4,3,2,1], 4) == [10,9,8,7,6,5,4]

# Test case 10
assert max_sliding_window([5,5,5,5,5], 2) == [5, 5, 5, 5]

print("All test cases passed!")