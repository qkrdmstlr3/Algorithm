"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10419
"""

import sys


def calculate(i):
    return i+i**2


for i in range(int(sys.stdin.readline())):
    d = int(sys.stdin.readline())
    index = 0
    while calculate(index+1) <= d:
        index += 1
    print(index)
