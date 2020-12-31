"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/2789
"""

import sys

word = list(sys.stdin.readline())
cam = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
result = []

for i in range(len(word)-1):
    if word[i] not in cam:
        result.append(word[i])
print(''.join(result))
