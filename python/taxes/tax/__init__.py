#!/usr/bin/env python3
"""
:URL:   https://www.codechef.com/submit/TAXES
"""


def calc_tax(income: int) -> int:
    if income <= 100:
        return income
    else:
        return income - 10


if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        income: int = int(input())
        print(calc_tax(income))
