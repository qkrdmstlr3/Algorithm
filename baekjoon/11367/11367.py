"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/11367
"""

import sys


def grade(s, n):
    if s >= 97:
        print(n, 'A+')
    elif s >= 90:
        print(n, 'A')
    elif s >= 87:
        print(n, 'B+')
    elif s >= 80:
        print(n, 'B')
    elif s >= 77:
        print(n, 'C+')
    elif s >= 70:
        print(n, 'C')
    elif s >= 67:
        print(n, 'D+')
    elif s >= 60:
        print(n, 'D')
    else:
        print(n, 'F')


for i in range(int(sys.stdin.readline())):
    name, score = sys.stdin.readline().split()
    grade(int(score), name)
