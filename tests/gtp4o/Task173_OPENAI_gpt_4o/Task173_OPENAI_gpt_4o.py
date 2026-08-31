from output.codestral.Task173_MISTRAL_codestral_latest import longest_dup_substring
from output.gemini.Task173_GEMINI_gemini_1_5_pro_001 import longestDupSubstring as longest_dup_substring
from output.gtp4o.Task173_OPENAI_gpt_4o import longestDupSubstring as longest_dup_substring
from output.llama3.Task173_PERPLEXITY_llama_3_sonar_large_32k_chat import longestDupSubstring as longest_dup_substring

assert longest_dup_substring("abcabcabcd") == "abcabc", longest_dup_substring("abcabcabcd")
assert longest_dup_substring("abababcababab") == "ababab", "Test Case 2 Failed"
assert longest_dup_substring("abacabadabacaba") == "abacaba", "Test Case 3 Failed"
assert longest_dup_substring("abcdefgabcdefgabcdefg") == "abcdefgabcdefg", "Test Case 4 Failed"
assert longest_dup_substring("aabbaabbaaccddcc") == "aabbaa", longest_dup_substring("aabbaabbaaccddcc")
assert longest_dup_substring("abcdabcdeabcdabcdeabcd") == "abcdabcdeabcd", "Test Case 6 Failed"
assert longest_dup_substring("abcdefghijklmnoabcdefghijklmno") == "abcdefghijklmno", "Test Case 7 Failed"
assert longest_dup_substring("xyzxyzxyzxyzx") == "xyzxyzxyzx", longest_dup_substring("xyzxyzxyzxyzx")
assert longest_dup_substring("abcdefgh12345678abcdefgh") == "abcdefgh", "Test Case 9 Failed"
assert longest_dup_substring("abcxabcyabczabcdabc") == "abc", longest_dup_substring("abcxabcyabczabcdabc")
print("All challenging test cases passed!")
