"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/3058
"""

import sys

for i in range(int(sys.stdin.readline())):
    data = list(map(int, sys.stdin.readline().split()))
    num_sum = []
    for i in data:
        if i % 2 == 0:
            num_sum.append(i)
    print(sum(num_sum), min(num_sum))
