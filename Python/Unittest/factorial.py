import unittest


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


class FactorialTest(unittest.TestCase):
   # def testFactZeroIsZero(self):
   #     self.assertEqual(1, fact(0))

   # def testFactOneIsOne(self):
   #     self.assertEqual(1, fact(1))

   # def testFactTwoIsTwo(self):
   #     self.assertEqual(2, fact(2))

   # def testFactThreeIsSix(self):
   #     self.assertEqual(6, fact(3))

   # def testFactFourIs24(self):
   #     self.assertEqual(24, fact(4))

    def testFactorial(self):
        di = {0:1, 1:1, 2:2, 3:6, 4:24}
        for key in di:
            expect = di[key]
            self.assertEqual(expect, fact(key))


if __name__ == "__main__":
    unittest.main()
