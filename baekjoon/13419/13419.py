"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13419
"""

import sys

for _ in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().rstrip()
    first, second = [], []
    for i in range(len(text)):
        if i % 2 == 0:
            first.append(text[i])
        else:
            second.append(text[i])
    if len(text) % 2 != 0:
        temp = first[:]
        first = first + second
        second = second + temp
    print(''.join(first))
    print(''.join(second))
        