# from output.claude.Task32_CLAUDE_claude_3_5_sonnet_20240620 import calculate_years as calculate_years
# from output.codestral.Task32_MISTRAL_codestral_latest import calculate_years as calculate_years
# from output.gemini.Task32_GEMINI_gemini_1_5_pro_001 import calculate_years as calculate_years
from output.gtp4o.Task32_OPENAI_gpt_4o import calculate_years as calculate_years
# from output.llama3.Task32_PERPLEXITY_llama_3_sonar_large_32k_chat import calculate_years as calculate_years
import unittest

def test_calculate_years():
    # Test case where it takes exactly 3 years to reach the desired sum
    assert calculate_years(1000.00, 0.05, 0.18, 1100.00) == 3

    # Test case where desired sum equals initial principal
    assert calculate_years(1000.00, 0.05, 0.18, 1000.00) == 0

    # Test case where it takes exactly 1 year to reach the desired sum
    assert calculate_years(1000.00, 0.05, 0.18, 1040.00) == 1

    # Test case where it takes many years to reach the desired sum
    assert calculate_years(1000.00, 0.05, 0.18, 2000.00) == 18

    # Test case where there is no tax on the interest
    assert calculate_years(1000.00, 0.05, 0.00, 2000.00) == 15

    # Test case where the tax rate is high
    assert calculate_years(1000.00, 0.05, 0.50, 2000.00) == 29

    # Test case with high interest and low tax rate
    assert calculate_years(1000.00, 0.10, 0.10, 2000.00) == 9

    # Test case with low interest and high tax rate
    assert calculate_years(1000.00, 0.02, 0.50, 2000.00) == 70

    # Test case where the interest rate is very small
    assert calculate_years(1000.00, 0.005, 0.18, 2000.00) == 170

    # Test case where both the principal and desired sum are very large
    assert calculate_years(1000000.00, 0.05, 0.18, 2000000.00) == 18

    print("All test cases passed!")

# Run the tests
test_calculate_years()