# from output.claude.Task167_CLAUDE_claude_3_5_sonnet_20240620 import cubeDiagonal as cube_diagonal
# from output.codestral.Task167_MISTRAL_codestral_latest import cubeDiagonal as cube_diagonal
# from output.gemini.Task167_GEMINI_gemini_1_5_pro_001 import cubeDiagonal as cube_diagonal
# from output.gtp4o.Task167_OPENAI_gpt_4o import cubeDiagonal as cube_diagonal
# from output.llama3.Task167_PERPLEXITY_llama_3_sonar_large_32k_chat import cubeDiagonal as cube_diagonal

import math

class TestCubeDiagonal:
    def test_case_1(self):
        assert round(cube_diagonal(8), 2) == 3.46

    def test_case_2(self):
        assert round(cube_diagonal(343), 2) == 12.12

    def test_case_3(self):
        assert round(cube_diagonal(1157.625), 2) == 18.19

    def test_case_4(self):
        assert round(cube_diagonal(27), 2) == 5.2

    def test_case_5(self):
        assert round(cube_diagonal(1), 2) == 1.73

    def test_case_6(self):
        assert round(cube_diagonal(64), 2) == 6.93

    def test_case_7(self):
        assert round(cube_diagonal(216), 2) == 10.39

    def test_case_8(self):
        assert round(cube_diagonal(1000), 2) == 17.32

    def test_case_9(self):
        assert round(cube_diagonal(0.125), 2) == 0.87

    def test_case_10(self):
        assert round(cube_diagonal(512), 2) == 13.86


# Example of running each test manually
test = TestCubeDiagonal()
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
print("all test good")