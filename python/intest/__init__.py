#!/usr/bin/env python3
"""
This is my solution to the codechef problem intest.
URL:            "https://www.codechef.com/LP0TO101/problems/INTEST"
Problem Code:   INTEST
Difficulty:     N/A
Author:         benni347@github.com
"""


def get_total():
    global total
    (n, k) = map(int, input().split(" "))
    for i in range(n):
        t = int(input())
        if t % k == 0:
            total += 1
    print(total)
    return total


total = 0

# k = divisor
# n = number of lines
# t = up
if __name__ == '__main__':
    get_total()
