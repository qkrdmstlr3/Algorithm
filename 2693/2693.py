"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2693
"""

import sys

for i in range(int(sys.stdin.readline())):
    array = list(map(int, sys.stdin.readline().split()))
    array.sort(reverse=True)
    print(array[2])
