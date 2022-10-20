#!/usr/bin/env python3
"""
:URL:	https://www.codechef.com/submit/TIMELY
"""


def can_reach(distance: int) -> str:
    possible: int = 30
    if distance >= possible:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        distance = int(input())
        can_reach(distance)

