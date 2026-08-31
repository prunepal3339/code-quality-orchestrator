# from output.codestral.Task169_MISTRAL_codestral_latest import count_smaller as countSmaller
# from output.gtp4o.Task169_OPENAI_gpt_4o import count_smaller as countSmaller
# from output.llama3.Task169_PERPLEXITY_llama_3_sonar_large_32k_chat import countSmaller as countSmaller

class TestCountSmaller:

    def test_case_1(self):
        assert countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]

    def test_case_2(self):
        assert countSmaller([-1]) == [0]

    def test_case_3(self):
        assert countSmaller([-1, -1]) == [0, 0]

    def test_case_4(self):
        assert countSmaller([1, 2, 3, 4]) == [0, 0, 0, 0]

    def test_case_5(self):
        assert countSmaller([4, 3, 2, 1]) == [3, 2, 1, 0]

    def test_case_6(self):
        assert countSmaller([2, 0, 1]) == [2, 0, 0]

    def test_case_7(self):
        assert countSmaller([10, 3, 2, 5]) == [3, 1, 0, 0]

    def test_case_8(self):
        assert countSmaller([1, 1, 1, 1]) == [0, 0, 0, 0]

    def test_case_9(self):
        assert countSmaller([6, 1, 2, 7, 1]) == [3, 0, 1, 1, 0]

    def test_case_10(self):
        assert countSmaller([5, 9, 2, 8, 6]) == [1, 3, 0, 1, 0]



# Example of running each test manually
test = TestCountSmaller()
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
print("all task good")