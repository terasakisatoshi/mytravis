import unittest
from myscript import MyClass

class MyClassTest(unittest.TestCase):

    def setUp(self):
        print("setup test")

    def test_first(self):
        print("test started")

    def test_myclass(self):
        klass=MyClass()
        self.assertTrue(klass.index())


def suite():
    suite=unittest.TestSuite()
    suite.addTests(unittest.makeSuite(MyClassTest))
    return suite