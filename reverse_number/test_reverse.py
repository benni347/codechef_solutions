import unittest
import reverse_number


class TestCaseReverse(unittest.TestCase):
    def test_reverse_positive(self):
        r = reverse_number.Reverse()
        r.n = "12"
        self.assertEqual(r.reverse_fn(), 21, "Should be 21")

    def test_reverse_negative(self):
        r = reverse_number.Reverse()
        r.n = "-12"
        self.assertEqual(r.reverse_fn(), -21, "Should be -21")

    def test_reverse_removed_zeroes(self):
        r = reverse_number.Reverse()
        r.n = "1200"
        self.assertEqual(r.reverse_fn(), 21, "Should be "
                                             "21")


if __name__ == '__main__':
    unittest.main()
