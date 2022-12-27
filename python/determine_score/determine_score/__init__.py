#!/usr/bin/env python3
"""
This is my solution to the codechef problem squats.
URL:            "https://www.codechef.com/problems/DETSCORE"
Problem Code:   DETSCORE
Difficulty:     267
Author:         benni347@github.com
"""


def calculate_the_total_score(problem: int, passed: int) -> int:
    """

    Parameters
    ----------
    passed: the amount of passed problems
    problem: is guaranteed to be a multible of 10

    Returns
    -------
    the total earned points
    int
    """
    multiplier: int = problem // 10
    earned_score: int = multiplier * passed
    return earned_score


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(test_cases):
        # normalized_input looks like this: `points pass`
        normalized_input = input()
        normalized_input = normalized_input.split()
        points: int = int(normalized_input[0])
        passed: int = int(normalized_input[1])
        print(calculate_the_total_score(points, passed))
