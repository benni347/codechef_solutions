#!/usr/bin/env python3
"""
This is my solution to the codechef problem squats.
URL:            "https://www.codechef.com/problems/SQUATS"
Problem Code:   SQUATS
Difficulty:     249
Author:         benni347@github.com
"""


def calculate_number_of_total_squats(amount_of_sets_done: int) -> int:
    """

    Parameters
    ----------
    amount_of_sets_done: a set is 15 squats so 1 -> 15

    Returns
    -------
    the total amount of squats done today
    int
    """
    total: int = amount_of_sets_done * 15
    return total


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(test_cases):
        sets: int = int(input())
        print(calculate_number_of_total_squats(sets))
