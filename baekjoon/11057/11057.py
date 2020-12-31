"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/11057
    correct percentage : 47.250%
    바로 이전 단계를 고려하면서 품
    다른 사람들보다 빠름
"""

import sys

N = int(sys.stdin.readline())
array = [[0]*10 for _ in range(N+1)]
array[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    num_sum = sum(array[i-1])
    array[i][0] = num_sum
    for j in range(1, 10):
        num_sum -= array[i-1][j-1]
        array[i][j] = num_sum
print(sum(array[N])%10007)
