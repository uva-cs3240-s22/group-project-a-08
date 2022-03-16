import unittest

class ExampleUnitTest(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(1,1)

    def test_example_2(self):
        self.assertNotEqual("hello","Hello")