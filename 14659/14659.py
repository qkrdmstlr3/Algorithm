"""
    Author : ParkEunsik
    Date   : 2019/09/05
    url    : https://www.acmicpc.net/problem/14659
"""

import sys

N = int(sys.stdin.readline())
peak = list(map(int, sys.stdin.readline().split()))
max_num = 0

for i in range(len(peak)):
    for j in range(i+1, len(peak)):
        if peak[j] > peak[i]:
            max_num = max(max_num, j-i-1)
            break
print(max_num)
