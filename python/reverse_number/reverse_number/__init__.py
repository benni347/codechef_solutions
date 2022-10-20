#!/usr/bin/env python3
"""
This is my solution to the codechef problem reverse number.
URL:            "https://www.codechef.com/LP0TO101/problems/FLOW007"
Problem Code:   FLOW007
Difficulty:     N/A
Author:         benni347@github.com
"""


class Reverse:
    def __init__(self):
        self.n = 0

    def get_number(self):
        self.n = str(input())
        self.reverse_fn()

    def reverse_fn(self):
        result = None
        is_negative = False
        if self.n[0] == "-":
            is_negative = True
            self.n = self.n.replace("-", "")
        result = list(reversed(self.n))
        if is_negative:
            result.insert(0, "-")
        result = "".join(map(str, result))
        result = int(result)

        print(result)
        return result


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        Reverse().get_number()
