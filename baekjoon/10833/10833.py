"""
    Author : ParkEunsik
    Date   : 2019/07/21
    url    : https://www.acmicpc.net/problem/10833
"""

import sys

cnt = 0
for i in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    cnt += m % n
print(cnt)
