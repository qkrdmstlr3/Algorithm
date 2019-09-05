"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/1449
"""

import sys

N, L = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))
wall = [True]*1001
count = 0
for i in leak:
    wall[i] = False

for i in range(1, max(leak)+1):
    if wall[i] is False:
        count += 1
        for j in range(i, i+L):
            if j > 1000:
                break
            wall[j] = True
print(count)
