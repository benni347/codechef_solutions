#!/usr/bin/env python3
"""
This is my solution to the codechef problem age limit.
URL:            "https://www.codechef.com/problems/AGELIMIT"
Problem Code:   AGELIMIT
Difficulty:     245
Author:         benni347@github.com
"""


def check_age_limit(lower_bound: int, upper_bound: int, current_age: int) -> str:
    """

    Parameters
    ----------
    lower_bound: int
    upper_bound: int
    current_age: int

    Returns
    -------
    a string "YES" or "NO" whether the current age is in the bound
    """
    if lower_bound <= current_age < upper_bound:
        return "YES"
    return "NO"


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(test_cases):
        # normalized_input looks like this: `lower_bound upper_bound current_age`
        normalized_input = input()
        normalized_input = normalized_input.split()
        lower: int = int(normalized_input[0])
        upper: int = int(normalized_input[1])
        current: int = int(normalized_input[2])
        print(check_age_limit(lower, upper, current))
