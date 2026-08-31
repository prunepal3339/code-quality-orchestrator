# from output.claude.Task169_CLAUDE_claude_3_5_sonnet_20240620 import Solution
from output.gemini.Task169_GEMINI_gemini_1_5_pro_001 import Solution

class TestCountSmaller:

    def test_case_1(self):
        solution = Solution()
        assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]

    def test_case_2(self):
        solution = Solution()
        assert solution.countSmaller([-1]) == [0]

    def test_case_3(self):
        solution = Solution()
        assert solution.countSmaller([-1, -1]) == [0, 0]

    def test_case_4(self):
        solution = Solution()
        assert solution.countSmaller([1, 2, 3, 4]) == [0, 0, 0, 0]

    def test_case_5(self):
        solution = Solution()
        assert solution.countSmaller([4, 3, 2, 1]) == [3, 2, 1, 0]

    def test_case_6(self):
        solution = Solution()
        assert solution.countSmaller([2, 0, 1]) == [2, 0, 0]

    def test_case_7(self):
        solution = Solution()
        assert solution.countSmaller([10, 3, 2, 5]) == [3, 1, 0, 0]

    def test_case_8(self):
        solution = Solution()
        assert solution.countSmaller([1, 1, 1, 1]) == [0, 0, 0, 0]

    def test_case_9(self):
        solution = Solution()

        assert solution.countSmaller([6, 1, 2, 7, 1]) == [3, 0, 1, 1, 0]

    def test_case_10(self):
        solution = Solution()
        assert solution.countSmaller([5, 9, 2, 8, 6]) == [1, 3, 0, 1, 0]



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