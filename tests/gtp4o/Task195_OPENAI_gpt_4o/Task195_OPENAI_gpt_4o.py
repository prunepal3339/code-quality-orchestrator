import unittest

from output.gtp4o.Task195_OPENAI_gpt_4o import MedianFinder


class Task195_OPENAI_gpt_4o(unittest.TestCase):

    def setUp(self):
        self.medianFinder = MedianFinder()

    def test_addNumAndFindMedian1(self):
        self.medianFinder.addNum(1)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 1.0, places=5)

    def test_addNumAndFindMedian2(self):
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(2)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 1.5, places=5)

    def test_addNumAndFindMedian3(self):
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(2)
        self.medianFinder.addNum(3)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 2.0, places=5)

    def test_addNumAndFindMedian4(self):
        self.medianFinder.addNum(3)
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(4)
        self.medianFinder.addNum(2)
        self.medianFinder.addNum(5)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 3.0, places=5)

    def test_addNumAndFindMedian5(self):
        self.medianFinder.addNum(10)
        self.medianFinder.addNum(5)
        self.medianFinder.addNum(15)
        self.medianFinder.addNum(20)
        self.medianFinder.addNum(25)
        self.medianFinder.addNum(30)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 17.5, places=5)

    def test_addNumAndFindMedian6(self):
        self.medianFinder.addNum(0)
        self.medianFinder.addNum(0)
        self.medianFinder.addNum(0)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 0.0, places=5)

    def test_addNumAndFindMedian7(self):
        self.medianFinder.addNum(-1)
        self.medianFinder.addNum(0)
        self.medianFinder.addNum(1)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 0.0, places=5)

    def test_addNumAndFindMedian8(self):
        self.medianFinder.addNum(-10)
        self.medianFinder.addNum(-20)
        self.medianFinder.addNum(-30)
        self.medianFinder.addNum(-40)
        self.medianFinder.addNum(-50)
        self.assertAlmostEqual(self.medianFinder.findMedian(), -30.0, places=5)

    def test_addNumAndFindMedian9(self):
        self.medianFinder.addNum(100)
        self.medianFinder.addNum(200)
        self.medianFinder.addNum(300)
        self.medianFinder.addNum(400)
        self.medianFinder.addNum(500)
        self.medianFinder.addNum(600)
        self.medianFinder.addNum(700)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 400.0, places=5)

    def test_addNumAndFindMedian10(self):
        self.medianFinder.addNum(1)
        self.medianFinder.addNum(3)
        self.medianFinder.addNum(2)
        self.medianFinder.addNum(4)
        self.medianFinder.addNum(5)
        self.medianFinder.addNum(6)
        self.medianFinder.addNum(7)
        self.medianFinder.addNum(8)
        self.medianFinder.addNum(9)
        self.assertAlmostEqual(self.medianFinder.findMedian(), 5.0, places=5)


if __name__ == '__main__':
    unittest.main()
