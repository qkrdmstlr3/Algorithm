"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/7568
    브루트포스
"""

import sys

li = []
result = []
for i in range(int(input())):
    li.append(list(map(int, sys.stdin.readline().split())))
    result.append(1)
for i in range(len(li)):
    for j in range(len(li)):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            result[i] += 1
for i in range(len(li)):
    print(result[i], end=' ')
