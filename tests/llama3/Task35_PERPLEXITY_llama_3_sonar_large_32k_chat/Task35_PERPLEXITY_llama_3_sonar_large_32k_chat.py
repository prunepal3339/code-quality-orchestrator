# from output.claude.Task35_CLAUDE_claude_3_5_sonnet_20240620 import number as count_passengers
# from output.codestral.Task35_MISTRAL_codestral_latest import bus_stops as count_passengers
# from output.gemini.Task35_GEMINI_gemini_1_5_pro_001 import number as count_passengers
# from output.gtp4o.Task35_OPENAI_gpt_4o import number_of_people as count_passengers
# from output.llama3.Task35_PERPLEXITY_llama_3_sonar_large_32k_chat import number_of_people_still_on_bus as count_passengers
import unittest
class TestTask35(unittest.TestCase):

    def test_single_stop(self):
        stops = [[10, 0]]
        self.assertEqual(count_passengers(stops), 10)

    def test_all_get_off(self):
        stops = [[10, 0], [3, 5], [2, 10]]
        self.assertEqual(count_passengers(stops), 0)

    def test_more_get_on_than_off(self):
        stops = [[5, 0], [7, 3], [4, 2]]
        self.assertEqual(count_passengers(stops), 11)

    def test_same_number_get_on_and_off(self):
        stops = [[3, 0], [2, 2], [0, 0]]
        self.assertEqual(count_passengers(stops), 3)

    def test_all_get_on_at_once(self):
        stops = [[20, 0], [0, 0], [0, 0]]
        self.assertEqual(count_passengers(stops), 20)

    def test_decreasing_passengers(self):
        stops = [[10, 0], [0, 3], [0, 5], [0, 2]]
        self.assertEqual(count_passengers(stops), 0)

    def test_empty_bus_stops(self):
        stops = [[10, 0], [0, 0], [0, 0]]
        self.assertEqual(count_passengers(stops), 10)

    def test_one_person_left(self):
        stops = [[1, 0], [0, 0]]
        self.assertEqual(count_passengers(stops), 1)

    def test_complex_scenario(self):
        stops = [[10, 0], [3, 5], [5, 8], [10, 2], [0, 3], [7, 3]]
        self.assertEqual(count_passengers(stops), 14)

    def test_large_numbers(self):
        stops = [[1000, 0], [500, 300], [200, 200], [300, 100]]
        self.assertEqual(count_passengers(stops), 1400)

if __name__ == "__main__":
    unittest.main()