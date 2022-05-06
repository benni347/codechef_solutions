#!/usr/bin/env python3
"""
This is my solution to the codechef problem farmers league.
URL:            "https://www.codechef.com/problems/LEAGUE"
Problem Code:   LEAGUE
Difficulty:     883
Author:         benni347@github.com
"""


class Main:
    """
    This is the main class.
    """

    def __init__(self) -> None:
        self.second_place_points = None
        self.teams = 0
        self.win_point = 3
        self.lose_point = 2
        self.first_place_points = None

    def get_teams_amount(self):
        """
        Get total teams and subtract two.
        """
        self.teams = int(input())
        # Subtract one so that no one wins against team one
        self.teams -= 1
        self.get_first_team_score()

    def get_first_team_score(self):
        """
        Get first team score.
        """
        self.first_place_points = self.teams * self.win_point
        self.get_min_to_get_second_place()

    def get_min_to_get_second_place(self):
        """
        Get the min points required for second place.
        """
        self.second_place_points = 3 * ((self.teams) // 2)
        self.get_result()

    def get_result(self):
        result = self.first_place_points - self.second_place_points
        print(result)
        return result
        # second_place_points = (self.teams - 2) * self.win_point


if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        Main().get_teams_amount()
