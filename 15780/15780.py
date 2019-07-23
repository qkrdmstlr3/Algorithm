"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/15780
"""

import sys

N, K = map(int, sys.stdin.readline().split())
multi = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(len(multi)):
    if multi[i] % 2 == 0:
        cnt += multi[i] // 2
    else:
        cnt += multi[i] // 2 + 1
if cnt >= N:
    print("YES")
else:
    print("NO")
