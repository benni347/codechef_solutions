#!/usr/bin/env python3
"""
This is my solution to the codechef problem Find Remainder.
URL:            "https://www.codechef.com/LP0TO101/problems/FLOW002"
Problem Code:   FLOW002
Difficulty:     N/A
Author:         benni347@github.com
"""


class Remainder:
    def __init__(self):
        self.a = 0
        self.b = 0

    def get_sizes(self):
        (self.a, self.b) = map(int, input().split(" "))
        self.divide()

    def divide(self):
        result = None
        self.a = int(self.a)
        self.b = int(self.b)
        if self.a < 0 or self.b < 0:
            result = -(-self.a // self.b)
        elif self.b == 0:
            result = "Mod and division is not available for divisor of 0."
        else:
            result = self.a % self.b
        print(result)
        return result


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        Remainder().get_sizes()
