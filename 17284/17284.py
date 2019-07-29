"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/17284
"""

import sys

cost = 5000
li = list(map(int, sys.stdin.readline().split()))
for i in range(len(li)):
    cost -= {1: 500, 2: 800, 3: 1000}[li[i]]
print(cost)
