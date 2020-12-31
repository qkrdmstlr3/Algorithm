"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/3460
"""

import sys

for i in range(int(sys.stdin.readline())):
    num = list(reversed(str(bin(int(sys.stdin.readline())))))
    for i in range(len(num)-2):
        if num[i] == '1':
            print(i, end='')
