import unittest

from determine_score import calculate_the_total_score


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_the_total_score(10, 3), 3)
        self.assertEqual(calculate_the_total_score(100, 10), 100)
        self.assertEqual(calculate_the_total_score(130, 4), 52)
        self.assertEqual(calculate_the_total_score(70, 0), 0)


if __name__ == '__main__':
    unittest.main()
