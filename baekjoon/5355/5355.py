"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/5355
"""

import sys

for i in range(int(sys.stdin.readline())):
    li = list(sys.stdin.readline().split())
    li[0] = float(li[0])
    for j in range(1, len(li)):
        if li[j] == '@':
            li[0] *= 3
        elif li[j] == '%':
            li[0] += 5
        elif li[j] == '#':
            li[0] -= 7
    print('{:0.2f}'.format(li[0]))
