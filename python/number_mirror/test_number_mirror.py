import unittest

from number_mirror import mirror


class MyTestCase(unittest.TestCase):
    def test_small(self):
        self.assertEqual(mirror(10), 10)
        self.assertEqual(mirror(1), 1)

    def test_big(self):
        self.assertEqual(mirror(12031234), 12031234)
        self.assertEqual(mirror(3438791487178348798971), 3438791487178348798971)


if __name__ == '__main__':
    unittest.main()
