# from output.claude.Task165_CLAUDE_claude_3_5_sonnet_20240620 import checkFlush as checkFlush
# from output.codestral.Task165_MISTRAL_codestral_latest import checkFlush as checkFlush
# from output.gemini.Task165_GEMINI_gemini_1_5_pro_001 import checkFlush as checkFlush
# from output.gtp4o.Task165_OPENAI_gpt_4o import checkFlush as checkFlush
# from output.llama3.Task165_PERPLEXITY_llama_3_sonar_large_32k_chat import checkFlush as checkFlush


class TestCheckFlush:
  def test_case_1(self):
    assert checkFlush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) == True

  def test_case_2(self):
    assert checkFlush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) == True

  def test_case_3(self):
    assert checkFlush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) == False

  def test_case_4(self):
    assert checkFlush(["2_H", "3_H", "4_H", "5_H", "6_D"], ["7_H", "8_H"]) == True

  def test_case_5(self):
    assert checkFlush(["9_S", "8_H", "7_D", "6_C", "5_S"], ["4_D", "3_H"]) == False

  def test_case_6(self):
    assert checkFlush(["K_C", "Q_C", "J_C", "9_C", "2_H"], ["8_C", "7_C"]) == True

  def test_case_7(self):
    assert checkFlush(["A_S", "2_S", "3_S", "4_H", "5_H"], ["6_S", "7_H"]) == False

  def test_case_8(self):
    assert checkFlush(["2_D", "3_D", "4_D", "5_D", "6_D"], ["7_H", "8_H"]) == True

  def test_case_9(self):
    assert checkFlush(["A_S", "K_H", "Q_D", "J_C", "10_S"], ["9_H", "8_C"]) == False

  def test_case_10(self):
    assert checkFlush(["A_S", "K_S", "Q_S", "J_S", "10_S"], ["9_S", "8_S"]) == True


# Implementing the checkFlush function
def checkFlush(table, hand):
  cards = table + hand
  suits = {}

  for card in cards:
    _, suit = card.split('_')
    if suit in suits:
      suits[suit] += 1
    else:
      suits[suit] = 1

  for count in suits.values():
    if count >= 5:
      return True
  return False

# Example of running each test manually
test = TestCheckFlush()
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
print("ALL GOOD")