"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/2998
"""

import sys

num = sys.stdin.readline().rstrip()
print(oct(int(num, 2))[2:])

