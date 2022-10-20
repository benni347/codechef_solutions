#!/usr/bin/env python3
"""
:URL:   https://www.codechef.com/submit/AUDIBLE
"""


def can_hear(frequency: int) -> str:
    lower_bound = 67
    upper_bound = 45000
    if lower_bound <= frequency <= upper_bound:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        frequency: int = int(input())
        print(can_hear(frequency))
