# from output.claude.Task15_CLAUDE_claude_3_5_sonnet_20240620 import tower_builder as tower_builder
# from output.codestral.Task15_MISTRAL_codestral_latest import tower_builder as tower_builder
# from output.gemini.Task15_GEMINI_gemini_1_5_pro_001 import tower_builder as tower_builder
# from output.gtp4o.Task15_OPENAI_gpt_4o import build_tower as tower_builder
# from output.llama3.Task15_PERPLEXITY_llama_3_sonar_large_32k_chat import tower_builder as tower_builder
import unittest
def tower_builder(n):
  # Generates a list of strings representing the tower with n floors
  return [
    ' ' * (n - i - 1) + '*' * (2 * i + 1) + ' ' * (n - i - 1)
    for i in range(n)
  ]

class TestTowerBuilder(unittest.TestCase):

  def test_one_floor(self):
    expected = ["*"]
    self.assertEqual(tower_builder(1), expected)

  def test_two_floors(self):
    expected = [
      " * ",
      "***"
    ]
    self.assertEqual(tower_builder(2), expected)

  def test_three_floors(self):
    expected = [
      "  *  ",
      " *** ",
      "*****"
    ]
    self.assertEqual(tower_builder(3), expected)

  def test_four_floors(self):
    expected = [
      "   *   ",
      "  ***  ",
      " ***** ",
      "*******"
    ]
    self.assertEqual(tower_builder(4), expected)

  def test_five_floors(self):
    expected = [
      "    *    ",
      "   ***   ",
      "  *****  ",
      " ******* ",
      "*********"
    ]
    self.assertEqual(tower_builder(5), expected)

  def test_six_floors(self):
    expected = [
      "     *     ",
      "    ***    ",
      "   *****   ",
      "  *******  ",
      " ********* ",
      "***********"
    ]
    self.assertEqual(tower_builder(6), expected)

  def test_seven_floors(self):
    expected = [
      "      *      ",
      "     ***     ",
      "    *****    ",
      "   *******   ",
      "  *********  ",
      " *********** ",
      "*************"
    ]
    self.assertEqual(tower_builder(7), expected)

  def test_eight_floors(self):
    expected = [
      "       *       ",
      "      ***      ",
      "     *****     ",
      "    *******    ",
      "   *********   ",
      "  ***********  ",
      " ************* ",
      "***************"
    ]
    self.assertEqual(tower_builder(8), expected)

  def test_nine_floors(self):
    expected = [
      "        *        ",
      "       ***       ",
      "      *****      ",
      "     *******     ",
      "    *********    ",
      "   ***********   ",
      "  *************  ",
      " *************** ",
      "*****************"
    ]
    self.assertEqual(tower_builder(9), expected)

  def test_ten_floors(self):
    expected = [
      "         *         ",
      "        ***        ",
      "       *****       ",
      "      *******      ",
      "     *********     ",
      "    ***********    ",
      "   *************   ",
      "  ***************  ",
      " ***************** ",
      "*******************"
    ]
    self.assertEqual(tower_builder(10), expected)

if __name__ == "__main__":
  unittest.main()