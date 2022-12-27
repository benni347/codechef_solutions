import unittest

from squats import calculate_number_of_total_squats


class MyTestCase(unittest.TestCase):
    def test_small(self):
        """
        Test numbers smaller 1000
        """
        self.assertEqual(calculate_number_of_total_squats(1), 15)
        self.assertEqual(calculate_number_of_total_squats(2), 30)
        self.assertEqual(calculate_number_of_total_squats(3), 45)
        self.assertEqual(calculate_number_of_total_squats(4), 60)

    def test_great(self):
        """
        test numbers greater 1000
        """
        self.assertEqual(calculate_number_of_total_squats(10000), 150000)
        self.assertEqual(calculate_number_of_total_squats(2000000), 30000000)
        self.assertEqual(calculate_number_of_total_squats(30000), 450000)
        self.assertEqual(calculate_number_of_total_squats(500000), 7500000)


if __name__ == '__main__':
    unittest.main()
