#!/usr/bin/env python3
import unittest
import league

# 2  # Team amount
# 3  # Team amount
# 4  # Team amount
# 9  # Team amount

"""
Expected:
3
3
6
12

"""


class TestScore(unittest.TestCase):

    def test_score_one(self):
        le = league.Main()
        le.teams = 9
        self.assertEqual(le.get_first_team_score(), "12", "Should be dif of 12")


if __name__ == '__main__':
    unittest.main()
