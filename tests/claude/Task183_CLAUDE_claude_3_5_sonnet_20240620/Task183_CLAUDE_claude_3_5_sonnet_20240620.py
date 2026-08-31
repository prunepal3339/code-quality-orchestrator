from output.claude.Task183_CLAUDE_claude_3_5_sonnet_20240620 import largest_series_product as largest_product
# from output.codestral.Task183_MISTRAL_codestral_latest import max_product as largest_product
# from output.gemini.Task183_GEMINI_gemini_1_5_pro_001 import largest_product
# from output.gtp4o.Task183_OPENAI_gpt_4o import find_largest_product as largest_product
# from output.llama3.Task183_PERPLEXITY_llama_3_sonar_large_32k_chat import largest_product
def test_largest_series_product():
    assert largest_product("63915", 3) == 162, "Test Case 1 Failed"
    assert largest_product("123456789", 2) == 72, "Test Case 2 Failed"
    assert largest_product("00000", 3) == 0, "Test Case 3 Failed"
    assert largest_product("987654321", 4) == 3024, "Test Case 4 Failed"
    assert largest_product("11111", 5) == 1, "Test Case 5 Failed"
    assert largest_product("123", 1) == 3, "Test Case 6 Failed"
    assert largest_product("99999", 5) == 59049, "Test Case 7 Failed"
    assert largest_product("56789", 2) == 72, "Test Case 8 Failed"
    assert largest_product("1234567890", 5) == 15120, "Test Case 9 Failed"
    assert largest_product("1", 1) == 1, "Test Case 10 Failed"

    print("All test cases passed!")

# Call the test function
test_largest_series_product()