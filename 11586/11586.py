"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/11586
"""

import sys

N = int(sys.stdin.readline())
mirror = []

for i in range(N):
    mirror.append(input())
K = int(sys.stdin.readline())
if K == 1:
    for i in range(N):
        print(mirror[i])
elif K == 2:
    for i in range(N):
        print(''.join(reversed(mirror[i])))
elif K == 3:
    for i in reversed(range(N)):
        print(mirror[i])
