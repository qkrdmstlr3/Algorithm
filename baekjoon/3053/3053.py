"""
    Author : ParkEunsik
    Date   : 2019/07/19
    url    : https://www.acmicpc.net/problem/3053
"""

import sys
import math

r = int(sys.stdin.readline())

pie = 3.141592

print('{:0.6f}'.format(math.pi*r*r))
print('{:0.6f}'.format(2*r*r))
