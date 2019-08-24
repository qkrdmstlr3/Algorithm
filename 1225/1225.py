"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1225
    correct percentage : 37.766%
"""

import sys

a, b = map(list, sys.stdin.readline().split())
a = map(int, a)
b = map(int, b)
print(sum(a)*sum(b))
