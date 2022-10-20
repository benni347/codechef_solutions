import unittest
from tax import calc_tax


class MyTestCase(unittest.TestCase):
    def test_smaller_100(self):
        test_data = ((5, 5), (10, 10), (100, 100), (99, 99))
        for variant, data in enumerate(test_data, start=1):
            income_test, expected = data
            with self.subTest(f'variation #{variant}', temp=income_test, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = calc_tax(income_test)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with I={income_test}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_greater_100(self):
        test_data = ((105, 95), (110, 100), (1100, 1090), (199, 189))
        for variant, data in enumerate(test_data, start=1):
            income_test, expected = data
            with self.subTest(f'variation #{variant}', temp=income_test, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = calc_tax(income_test)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with I={income_test}')
                self.assertEqual(actual_result, expected, failure_message)


if __name__ == '__main__':
    unittest.main()
