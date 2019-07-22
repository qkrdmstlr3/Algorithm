"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/13458
    correct percentage : 24.198%
"""

import sys
import math

N = int(sys.stdin.readline())
cnt = N
student = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

for i in range(N):
    student[i] -= B
    if student[i] > 0:
        cnt += math.ceil(student[i]/C)
print(cnt)
