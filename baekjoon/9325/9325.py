"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/9325
"""

import sys

for i in range(int(sys.stdin.readline())):
    s = int(sys.stdin.readline())
    price = s
    for j in range(int(sys.stdin.readline())):
        q, p = map(int, sys.stdin.readline().split())
        price += q*p
    print(price)
