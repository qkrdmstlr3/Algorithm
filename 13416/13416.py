"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13416
"""

import sys

for _ in range(int(sys.stdin.readline())):
    num_sum = 0
    for _ in range(int(sys.stdin.readline())):
        zusik = list(map(int, sys.stdin.readline().split()))
        max_zusik = max(zusik)
        if max_zusik > 0:
            num_sum += max_zusik
    print(num_sum)
