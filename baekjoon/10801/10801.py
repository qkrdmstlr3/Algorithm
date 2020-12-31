"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/10801
"""

import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(10):
    if A[i] < B[i]:
        cnt += 1
    elif A[i] > B[i]:
        cnt -= 1
if cnt > 0:
    print("B")
elif cnt < 0:
    print("A")
else:
    print("D")
