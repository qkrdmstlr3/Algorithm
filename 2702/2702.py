"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/2702
"""

import sys
from fractions import gcd

for i in range(int(sys.stdin.readline())):
    li = sorted(list(map(int, sys.stdin.readline().split())))
    if li[1] % li[0] == 0:
        print(li[1], li[0])
    else:
        print(li[0]*li[1]//gcd(li[0], li[1]), gcd(li[0], li[1]))
