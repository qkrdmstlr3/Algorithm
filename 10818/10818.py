"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10818
"""

import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
print(num[0], num[-1])
