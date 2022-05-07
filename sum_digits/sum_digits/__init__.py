#!/usr/bin/env python3
"""
This is my solution to the codechef problem sum of digits.
URL:            "https://www.codechef.com/LP0TO101/problems/FLOW006"
Problem Code:   FLOW006
Difficulty:     N/A
Author:         benni347@github.com
"""


class Sum:
    def __init__(self):
        self.num = None

    def get_int(self):
        self.num = int(input())
        self.get_sum()

    def get_sum(self):
        result = None
        if self.num < 0:
            result = "Only numbers above 0 work."
        else:
            result = 0
            for i in str(self.num):
                num = int(i)

                result = int(result + num)
        print(result)
        return result


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        Sum().get_int()
