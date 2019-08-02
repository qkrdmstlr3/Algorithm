"""
    Author : ParkEunsik
    Date   : 2019/08/02
    url    : https://www.acmicpc.net/problem/2810
"""

import sys

N = int(sys.stdin.readline())
chair = input()
cupholder_count = 1
couple_chair_count = 1
if 'L' not in chair:
    cupholder_count = N
else:
    for i in range(N):
        if couple_chair_count == 2 and chair[i-1] == 'L':
            couple_chair_count = 1
            continue
        if chair[i-1] == 'L':
            couple_chair_count += 1
        cupholder_count += 1
print(cupholder_count)
