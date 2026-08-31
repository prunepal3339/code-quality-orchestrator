# from output.claude.Task168_CLAUDE_claude_3_5_sonnet_20240620 import tweakLetters as tweakLetters
# from output.codestral.Task168_MISTRAL_codestral_latest import tweakLetters as tweakLetters
# from output.gemini.Task168_GEMINI_gemini_1_5_pro_001 import tweakLetters as tweakLetters
# from output.gtp4o.Task168_OPENAI_gpt_4o import tweak_letters  as tweakLetters
# from output.llama3.Task168_PERPLEXITY_llama_3_sonar_large_32k_chat import tweakLetters as tweakLetters


class TestTweakLetters:
  def test_case_1(self):
    assert tweakLetters("apple", [0, 1, -1, 0, -1]) == "aqold"

  def test_case_2(self):
    assert tweakLetters("many", [0, 0, 0, -1]) == "manx"

  def test_case_3(self):
    assert tweakLetters("rhino", [1, 1, 1, 1, 1]) == "sijop"

  def test_case_4(self):
    assert tweakLetters("abc", [1, 1, 1]) == "bcd"

  def test_case_5(self):
    assert tweakLetters("xyz", [1, 1, 1]) == "yza"

  def test_case_6(self):

    assert tweakLetters("hello", [-1, 0, 1, 0, -1]) == "gemln"

  def test_case_7(self):
    assert tweakLetters("test", [-1, -1, -1, -1]) == "sdrs"

  def test_case_8(self):
    assert tweakLetters("abcd", [1, 2, 3, 4]) == "bdfh"

  def test_case_9(self):
    assert tweakLetters("zzz", [-1, -1, -1]) == "yyy"

  def test_case_10(self):

    assert tweakLetters("world", [0, 1, -1, 2, -2]) == "wpqnb"


# Example of running each test manually
test = TestTweakLetters()
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
print("all Task Good")