"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/3076
"""
import sys

r, c = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())
black_start, white_start = "", ""

for i in range(c):
    if i % 2 == 0:
        black_start += 'X'*b
        white_start += '.'*b
    else:
        black_start += '.'*b
        white_start += 'X'*b
for i in range(r):
    for j in range(a):
        if i % 2 == 0:
            print(black_start)
        else:
            print(white_start)
