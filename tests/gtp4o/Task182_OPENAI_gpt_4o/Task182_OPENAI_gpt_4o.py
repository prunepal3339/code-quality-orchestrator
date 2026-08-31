
# from output.claude.Task182_CLAUDE_claude_3_5_sonnet_20240620 import clean_phone_number
# from output.codestral.Task182_MISTRAL_codestral_latest import clean_phone_number
# from output.gemini.Task182_GEMINI_gemini_1_5_pro_001 import clean_phone_number
from output.gtp4o.Task182_OPENAI_gpt_4o import clean_number as clean_phone_number
# from output.llama3.Task182_PERPLEXITY_llama_3_sonar_large_32k_chat import clean_phone_number
# Test cases
assert clean_phone_number('+1 (613)-995-0253') == '6139950253'
assert clean_phone_number('613-995-0253') == '6139950253'
assert clean_phone_number('1 613 995 0253') == '6139950253'
assert clean_phone_number('613.995.0253') == '6139950253'
assert clean_phone_number('6139950253') == '6139950253'
assert clean_phone_number('  +1  613  995  0253  ') == '6139950253'  # Extra spaces
assert clean_phone_number('(613) 995-0253') == '6139950253'  # Parentheses only
assert clean_phone_number('1-613-995-0253') == '6139950253'  # Hyphens only
assert clean_phone_number('1 613.995 0253') == '6139950253'  # Mixed separators
assert clean_phone_number('613 995 0253') == '6139950253'  # Spaces only

print("All tests passed!")