"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10179
"""

import sys

for _ in range(int(sys.stdin.readline())):
    price = float(sys.stdin.readline())
    print('${:0.2f}'.format(round(price*80/100, 2)))
