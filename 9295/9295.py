"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/9295
"""

import sys

for i in range(int(sys.stdin.readline())):
    print("Case ", i+1, ": ", sum(map(int, sys.stdin.readline().split())), sep='')
