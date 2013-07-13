'''
A simple script show some popular method in unittest
'''
import unittest


def setUpModule():
    print "Start testing"


def tearDownModule():
    print "Tearing down testing and stop script"


class TestStupid(unittest.TestCase):
    def setUp(self):
        self.xxx = 5
        print "setUp In " + str(self.__class__),  self.xxx

    def tearDown(self):
        print "tearDown In " + str(self.__class__),  self.xxx
        del self.xxx

    def test_xxx_is_5(self):
        self.assertEqual(self.xxx, 5, "Nha co ma")

    def test_xxx_is_smaller_than_6(self):
        self.assertTrue(self.xxx < 6)


class TestDump(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "Class {0} is running".format(cls.__name__)

    @classmethod
    def tearDownClass(cls):
        print "Done test for {0} class".format(cls.__name__)

    def test_foo(self):
        self.assertTrue(1 == 1)


if __name__ == "__main__":
    unittest.main()
