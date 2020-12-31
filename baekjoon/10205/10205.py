"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10205
"""

import sys

for j in range(int(sys.stdin.readline())):
    h = int(sys.stdin.readline())
    for i in sys.stdin.readline().rstrip():
        if i == 'c':
            h += 1
        elif i == 'b':
            h -= 1
    print("Data Set ", j+1, ":", sep='')
    print(h)
    print()
