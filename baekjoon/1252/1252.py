"""
    Author : ParkEunsik
    Date   : 2019/09/18
    url    : https://www.acmicpc.net/problem/1247
    correct percentage : 27.606%
"""

import sys

a, b = sys.stdin.readline().split()

num_sum = int(a, 2)+ int(b, 2)
print(bin(num_sum)[2:])
