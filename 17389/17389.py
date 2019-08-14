"""
    Author : ParkEunsik
    Date   : 2019/08/15
    url    : https://www.acmicpc.net/problem/17389
"""

import sys

N = int(sys.stdin.readline())
ox = input()
score, bonus = 0, 0

for i in range(len(ox)):
    if ox[i] == 'X':
        bonus = 0
        continue
    score += bonus+i+1
    bonus += 1
print(score)
