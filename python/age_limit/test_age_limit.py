import unittest

from age_limit import check_age_limit


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(check_age_limit(21, 34, 30), "YES")  # add assertion here
        self.assertEqual(check_age_limit(34, 39, 36), "YES")  # add assertion here
        self.assertEqual(check_age_limit(20, 22, 20), "YES")  # add assertion here

    def test_false_smaller_lower_bound(self):
        self.assertEqual(check_age_limit(21, 34, 20), "NO")  # add assertion here
        self.assertEqual(check_age_limit(34, 39, 33), "NO")  # add assertion here
        self.assertEqual(check_age_limit(20, 22, 19), "NO")  # add assertion here

    def test_false_greater_upper_bound(self):
        self.assertEqual(check_age_limit(21, 34, 35), "NO")  # add assertion here
        self.assertEqual(check_age_limit(34, 39, 40), "NO")  # add assertion here
        self.assertEqual(check_age_limit(20, 22, 23), "NO")  # add assertion here

    def test_false_equal_upper_bound(self):
        self.assertEqual(check_age_limit(21, 34, 34), "NO")  # add assertion here
        self.assertEqual(check_age_limit(34, 39, 39), "NO")  # add assertion here
        self.assertEqual(check_age_limit(20, 22, 22), "NO")  # add assertion here


if __name__ == '__main__':
    unittest.main()
