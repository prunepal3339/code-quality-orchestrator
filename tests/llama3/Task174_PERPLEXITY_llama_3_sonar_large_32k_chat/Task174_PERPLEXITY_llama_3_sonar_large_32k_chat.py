from output.codestral.Task174_MISTRAL_codestral_latest import shortest_palindrome
from output.gtp4o.Task174_OPENAI_gpt_4o import  shortest_palindrome as shortest_palindrome
from output.llama3.Task174_PERPLEXITY_llama_3_sonar_large_32k_chat import shortestPalindrome as shortest_palindrome

assert shortest_palindrome("racecar") == "racecar", "Test Case 1 Failed"
assert shortest_palindrome("aacecaaa") == "aaacecaaa", "Test Case 2 Failed"
assert shortest_palindrome("abcd") == "dcbabcd", "Test Case 3 Failed"
assert shortest_palindrome("") == "", "Test Case 4 Failed"
assert shortest_palindrome("a") == "a", "Test Case 5 Failed"
assert shortest_palindrome("aaaaaaaa") == "aaaaaaaa", "Test Case 6 Failed"
assert shortest_palindrome("abcda") == "adcbaabcda", "Test Case 7 Failed: " + shortest_palindrome("abcda")
assert shortest_palindrome("ababababab") == "bababababab", "Test Case 8 Failed"
assert shortest_palindrome("xyz") == "zyxyz", "Test Case 9 Failed"
assert shortest_palindrome("abbaac") == "caabbaac", "Test Case 10 Failed"

print("All test cases passed!")