"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/2003
    합을 매번 계산하지 않도록 개선 해보기
"""

import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
count = 0
index1, index2 = 0, 0
num_sum = 0

while index2 < N:
    if sum(array[index1:index2+1]) == M:
        count += 1
        index1 += 1
    elif sum(array[index1:index2+1]) > M:
        index1 += 1
    else:
        index2 += 1
print(count)
