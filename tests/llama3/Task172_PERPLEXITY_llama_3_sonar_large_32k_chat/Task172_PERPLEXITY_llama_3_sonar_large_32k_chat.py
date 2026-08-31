from output.codestral.Task172_MISTRAL_codestral_latest import numDistinct
from output.gtp4o.Task172_OPENAI_gpt_4o import distinct_aa_substrings as numDistinct
from output.llama3.Task172_PERPLEXITY_llama_3_sonar_large_32k_chat import distinctEchoSubstrings as numDistinct

assert numDistinct("abcabcabc") == 3, "Test Case 1 Failed"  # "abcabc", "bcabca", "cabcab"
assert numDistinct("leetcodeleetcode") == 2, "Test Case 2 Failed"  # "ee", "leetcodeleetcode"
assert numDistinct("a") == 0, "Test Case 3 Failed"  # No echo substrings
assert numDistinct("aa") == 1, "Test Case 4 Failed"  # "aa"
assert numDistinct("aaa") == 1, "Test Case 5 Failed"  # "aa"
assert numDistinct("abab") == 2, "Test Case 6 Failed"  # "abab", "ab"
assert numDistinct("abcde") == 0, "Test Case 7 Failed"  # No echoes
assert numDistinct("abababab") == 4, "Test Case 8 Failed"  # "abab", "baba", "abababab"
assert numDistinct("abcabcabcabc") == 6, "Test Case 9 Failed"  # "abcabc", "bcabca", "cabcab", "abcabcabc", "bca", "cab"

print("All test cases passed!")