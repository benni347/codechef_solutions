#!/usr/bin/env python3
"""
This is my solution to the codechef problem Who is taller!.
URL:            "https://www.codechef.com/LP0TO101/problems/CHOPRT"
Problem Code:   CHOPRT
Difficulty:     N/A
Author:         benni347@github.com
"""


class Operations:
    def __init__(self):
        self.a = 0
        self.b = 0

    def get_values(self):
        (self.a, self.b) = map(int, input().split(" "))
        self.get_operator()

    def get_operator(self):
        result = ""
        if self.a < self.b:
            result = "<"
        elif self.a > self.b:
            result = ">"
        elif self.a == self.b:
            result = "="
        else:
            result = "Not a standard operator"
        print(result)
        return result


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        Operations().get_values()
