# from output.claude.Task166_CLAUDE_claude_3_5_sonnet_20240620 import posNegSort as posNegSort
# from output.codestral.Task166_MISTRAL_codestral_latest import posNegSort as posNegSort
# from output.gemini.Task166_GEMINI_gemini_1_5_pro_001 import posNegSort as posNegSort
# from output.gtp4o.Task166_OPENAI_gpt_4o import posNegSort as posNegSort
# from output.llama3.Task166_PERPLEXITY_llama_3_sonar_large_32k_chat import posNegSort as posNegSort

class TestPosNegSort:
  def test_case_1(self):
    assert posNegSort([6, 3, -2, 5, -8, 2, -2]) == [2, 3, -2, 5, -8, 6, -2]

  def test_case_2(self):
    assert posNegSort([6, 5, 4, -1, 3, 2, -1, 1]) == [1, 2, 3, -1, 4, 5, -1, 6]

  def test_case_3(self):
    assert posNegSort([-5, -5, -5, -5, 7, -5]) == [-5, -5, -5, -5, 7, -5]

  def test_case_4(self):
    assert posNegSort([]) == []

  def test_case_5(self):
    assert posNegSort([10, -10, 20, -20]) == [10, -10, 20, -20]

  def test_case_6(self):
    assert posNegSort([9, 3, -3, -2, 7]) == [3, 7, -3, -2, 9]

  def test_case_7(self):
    assert posNegSort([5, 4, -1, -2, 1]) == [1, 4, -1, -2, 5]

  def test_case_8(self):
    assert posNegSort([-3, -2, -1]) == [-3, -2, -1]

  def test_case_9(self):
    assert posNegSort([100, -50, 75, -25]) == [75, -50, 100, -25]

  def test_case_10(self):
    assert posNegSort([2, 1, -9, -8]) == [1, 2, -9, -8]


# Implementing the posNegSort function
def posNegSort(arr):
  # Extract positive numbers and sort them
  positive_numbers = sorted([x for x in arr if x > 0])
  # Create an iterator for the sorted positive numbers
  pos_iter = iter(positive_numbers)

  # Replace positive numbers in the original array with sorted ones
  return [next(pos_iter) if x > 0 else x for x in arr]


# Example of running each test manually
test = TestPosNegSort()
test.test_case_1()
test.test_case_2()
test.test_case_3()
test.test_case_4()
test.test_case_5()
test.test_case_6()
test.test_case_7()
test.test_case_8()
test.test_case_9()
test.test_case_10()

print ("ALL GOOD")