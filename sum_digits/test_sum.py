import unittest
import sum_digits


class TestSum(unittest.TestCase):
    def test_sum_positive_int(self):
        s = sum_digits.Sum()
        s.num = 12345
        self.assertEqual(s.get_sum(), 15, "Should be 15")

    def test_sum_negative_int(self):
        s = sum_digits.Sum()
        s.num = -12345
        self.assertEqual(s.get_sum(), 'Only numbers above 0 work.', "Should be Error")

    def test_sum_zero(self):
        s = sum_digits.Sum()
        s.num = 0
        self.assertEqual(s.get_sum(), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()
