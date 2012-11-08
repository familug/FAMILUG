import unittest

class FirstTest(unittest.TestCase):

    def test(self):
        self.failUnless(True)

    def testPass(self):
        return

    def testFail(self):
        self.failIf(True)

    def testErr(self):
        raise KeyError("hohoho")
        

if __name__ == "__main__":
    unittest.main()

