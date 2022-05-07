import unittest
import remainder


class TestRemainder(unittest.TestCase):
    def test_remainder_1(self):
        r = remainder.Remainder()
        r.a = 1
        r.b = 2
        self.assertEqual(r.divide(), 1, "Should be 1")

    def test_remainder_negative_num_numerator(self):
        r = remainder.Remainder()
        r.a = -1
        r.b = 2
        self.assertEqual(r.divide(), 0, "Should be 0")

    def test_remainder_negative_num_divisor(self):
        r = remainder.Remainder()
        r.a = 2
        r.b = -10
        self.assertEqual(r.divide(), 0, "Should be 0")

    def test_remainder_str(self):
        r = remainder.Remainder()
        r.a = 11
        r.b = "2"
        self.assertEqual(r.divide(), 1, "Should be 1")

    def test_forty_div_fifteen(self):
        r = remainder.Remainder()
        r.a = 40
        r.b = 15
        self.assertEqual(r.divide(), 10, "Should be 10")

    def test_zero_numerator(self):
        r = remainder.Remainder()
        r.a = 0
        r.b = 15
        self.assertEqual(r.divide(), 0, "Should be 0")

    def test_zero_divisor(self):
        r = remainder.Remainder()
        r.a = 15
        r.b = 0
        self.assertEqual(r.divide(), 'Mod and division is not available for divisor of 0.', "Should be 'Mod and "
                                                                                            "division is not "
                                                                                            "available for divisor of "
                                                                                            "0.' ")


if __name__ == '__main__':
    unittest.main()
