"""
    Author : ParkEunsik
    Date   : 2019/07/17
    url    : https://www.acmicpc.net/problem/11047
"""

import sys

N, K = map(int, sys.stdin.readline().split())
arr, cnt = [], 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

for i in reversed(range(len(arr))):
    if arr[i] > K:
        continue
    cnt += K // arr[i]
    K = K % arr[i]
print(cnt)
