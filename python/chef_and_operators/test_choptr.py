import unittest
import choprt


class TestChoprt(unittest.TestCase):
    def test_smaller_than(self):
        c = choprt.Operations()
        c.a = 10
        c.b = 20
        self.assertEqual(c.get_operator(), "<", "Should be <")

    def test_bigger_than(self):
        c = choprt.Operations()
        c.a = 90
        c.b = 20
        self.assertEqual(c.get_operator(), ">", "Should be >")


if __name__ == '__main__':
    unittest.main()
