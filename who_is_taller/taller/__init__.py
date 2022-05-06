#!/usr/bin/env python3
"""
This is my solution to the codechef problem Who is taller!.
URL:            "https://www.codechef.com/problems/TALLER"
Problem Code:   TALLER
Difficulty:     281
Author:         benni347@github.com
"""


class Taller:
    def __init__(self):
        self.a = 100
        self.b = 100

    def get_sizes(self):
        (self.a, self.b) = map(int, input().split(" "))
        self.get_taller()

    def get_taller(self):
        result = ""
        if self.a > self.b:
            result = "A"
        else:
            result = "B"
        print(result)
        return result


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        Taller().get_sizes()
