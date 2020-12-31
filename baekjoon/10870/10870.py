"""
    Author : ParkEunsik
    Date   : 2019/09/07
    url    : https://www.acmicpc.net/problem/10870
"""

import sys

n = int(sys.stdin.readline())

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(n))
