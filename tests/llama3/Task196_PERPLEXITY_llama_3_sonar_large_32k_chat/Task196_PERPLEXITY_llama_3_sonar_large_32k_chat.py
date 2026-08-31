import unittest
import threading

from output.llama3.Task196_PERPLEXITY_llama_3_sonar_large_32k_chat import ZeroEvenOdd


class Task196_PERPLEXITY_llama_3_sonar_large_32k_chat(unittest.TestCase):

    def run_test(self, n, expected):
        output = []

        def printNumber(x):
            output.append(str(x))

        zeo = ZeroEvenOdd(n)
        threads = [
            threading.Thread(target=zeo.zero, args=(printNumber,)),
            threading.Thread(target=zeo.even, args=(printNumber,)),
            threading.Thread(target=zeo.odd, args=(printNumber,))
        ]

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        self.assertEqual("".join(output), expected)

    def test_case_1(self):
        self.run_test(1, "01")

    def test_case_2(self):
        self.run_test(2, "0102")

    def test_case_3(self):
        self.run_test(3, "010203")

    def test_case_4(self):
        self.run_test(4, "01020304")

    def test_case_5(self):
        self.run_test(5, "0102030405")

    def test_case_6(self):
        self.run_test(6, "010203040506")

    def test_case_7(self):
        self.run_test(7, "01020304050607")

    def test_case_8(self):
        self.run_test(8, "0102030405060708")

    def test_case_9(self):
        self.run_test(9, "010203040506070809")

    def test_case_10(self):
        self.run_test(10, "010203040506070809010")

if __name__ == "__main__":
    unittest.main()
