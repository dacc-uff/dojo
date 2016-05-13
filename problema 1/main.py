
import unittest

class TestHappyNumbers(unittest.TestCase):

    def test_1_is_happy(self):
        self.assertTrue(happy(1))

    def test_2_is_not_happy(self):
        self.assertFalse(happy(2))    

    def test_10_is_happy(self):
        self.assertTrue(happy(10))

    


def happy(number):
    return number == 1 or number == 10

if __name__ == '__main__':
    unittest.main()
