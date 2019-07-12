"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/2562
"""

import sys

index, mx = 0, 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > mx:
        mx, index = num, i
print(mx, index, sep='\n')
