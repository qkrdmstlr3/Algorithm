"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1676
    correct percentage : 37.794%
"""

import sys

N = int(sys.stdin.readline())
print(N//5 + N//25+ N//125)
