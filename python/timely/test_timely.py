import unittest
from timely import can_reach


class MyTestCase(unittest.TestCase):
    def test_possible(self):
        test_data = ((30, "YES"), (60, "YES"), (40, "YES"), (50, "YES"))
        for variant, data in enumerate(test_data, start=1):
            distance, expected = data
            with self.subTest(f'variation #{variant}', dist=distance, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_reach(distance)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with D={distance}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_not_possible(self):
        test_data = ((29, "NO"), (6, "NO"), (14, "NO"), (15, "NO"))
        for variant, data in enumerate(test_data, start=1):
            distance, expected = data
            with self.subTest(f'variation #{variant}', dist=distance, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = can_reach(distance)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'with D={distance}')
                self.assertEqual(actual_result, expected, failure_message)


if __name__ == '__main__':
    unittest.main()
