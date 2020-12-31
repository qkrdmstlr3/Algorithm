"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1120
"""

import sys

a, b = sys.stdin.readline().split()
min_count = 100

for i in range(len(b)-len(a)+1):
    count = 0
    check = b[i:len(a)+i]
    for j in range(len(a)):
        if a[j] != check[j]:
            count += 1
    min_count = min(min_count, count)
print(min_count)
