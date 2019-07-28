"""
    Author : ParkEunsik
    Date   : 2019/07/06
    url    : https://www.acmicpc.net/problem/17362
"""

import sys

num = int(sys.stdin.readline())

li = [[1], [2, 0], [3, 7], [4, 6], [5]]
for i in range(5):
    if num % 8 in li[i]:
        print(i+1)
