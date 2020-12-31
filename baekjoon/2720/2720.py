"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2720
"""

import sys

for _ in range(int(sys.stdin.readline())):
    price = [25, 10, 5]
    C = int(sys.stdin.readline())
    for i in price:
        print(C//i, end=' ')
        C %= i
    print(C)
