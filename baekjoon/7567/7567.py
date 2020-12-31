"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/7567
"""

import sys

disk, height = sys.stdin.readline(), 10

for i in range(1, len(disk)-1):
    if disk[i] == disk[i-1]:
        height += 5
    else:
        height += 10
print(height)
