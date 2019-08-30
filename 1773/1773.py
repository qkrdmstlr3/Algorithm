"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/1773
"""

import sys

N, C = map(int, sys.stdin.readline().split())
firework = set()
for i in range(N):
    time = int(sys.stdin.readline())
    if time in firework:
        continue
    for j in range(time, C+1, time):
        firework.add(j)
print(len(firework))
