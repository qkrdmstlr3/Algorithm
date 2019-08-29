"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5800
"""

import sys

for i in range(int(sys.stdin.readline())):
    array = list(map(int, sys.stdin.readline().split()))
    array.pop(0)
    print("Class", i+1)
    print("Max ", max(array), ", Min ", min(array), ", Largest gap ", sep='', end='')
    max_gap = 0
    array.sort()
    for j in range(len(array)-1):
        max_gap = max(max_gap, array[j+1]-array[j])
    print(max_gap)
