"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2563
"""

import sys

paper = [[False]*100 for _ in range(100)]
size = 0
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    for m in range(10):
        for n in range(10):
            if paper[a+m][b+n]:
                continue
            paper[a+m][b+n] = True
            size += 1
print(size)
