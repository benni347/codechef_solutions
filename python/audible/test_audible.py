import unittest
from audible import can_hear


class MyTestCase(unittest.TestCase):
    def test_smaller(self):
        test_data = ((10, "NO"), (20, "NO"), (25, "NO"))
        for variant, data in enumerate(test_data, start=1):
            frequency, expected = data
            with self.subTest(f'variation #{variant}', freq=frequency, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_hear(frequency)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with F={frequency}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_greater(self):
        test_data = ((46001, "NO"), (200000, "NO"), (50000, "NO"))
        for variant, data in enumerate(test_data, start=1):
            frequency, expected = data
            with self.subTest(f'variation #{variant}', freq=frequency, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_hear(frequency)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with F={frequency}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_between(self):
        test_data = ((44000, "YES"), (80, "YES"), (1000, "YES"))
        for variant, data in enumerate(test_data, start=1):
            frequency, expected = data
            with self.subTest(f'variation #{variant}', freq=frequency, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_hear(frequency)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with F={frequency}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_edge_case(self):
        test_data = ((45000, "YES"), (67, "YES"), (66, "NO"), (45001, "NO"))
        for variant, data in enumerate(test_data, start=1):
            frequency, expected = data
            with self.subTest(f'variation #{variant}', freq=frequency, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_hear(frequency)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with F={frequency}')
                self.assertEqual(actual_result, expected, failure_message)




if __name__ == '__main__':
    unittest.main()
