"""
    Author : ParkEunsik
    Date   : 2019/09/20
    url    : https://www.acmicpc.net/problem/2846
    correct percentage: 41.257%
"""

import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))

max_num = 0
for i in range(N):
    temp = 0
    for j in range(i+1, N):
        if road[i] >= road[j] or road[j] <= road[j-1]:
            break
        temp = j
        max_num = max(max_num, road[temp] - road[i])
print(max_num)
