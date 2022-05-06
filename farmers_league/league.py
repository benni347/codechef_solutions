#!/usr/bin/env python3
"""
This is my solution to the codechef problem farmers leaque.
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
        self.teams = 0
        self.win_point = 3
        self.lose_point = 2
        self.first_place_points = 0

    def get_teams_amount(self):
        """
        Get total teamand subtract two.
        """
        self.teams = int(input())
        # Subtract two so that no one wins against team one and one so it doesn't loose to itself.
        self.teams -= 2

    def get_first_team_score(self):
        """
        Get first team score.
        """
        self.first_place_points = (self.teams + 1) * self.win_point

    def get_min_to_get_second_place(self):
        """
        Get the min points required for second place.
        """

        # first_place_points = (self.teams - 1) * self.win_point
        # second_place_points = (self.teams - 2) * self.win_point
        # print("First place: " + str(first_place_points))
        # print("Second place: " + str(second_place_points))
        # print(first_place_points - second_place_points)


if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        Main().get_teams_amount()
