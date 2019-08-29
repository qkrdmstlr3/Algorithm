"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5176
"""

import sys

for i in range(int(sys.stdin.readline())):
    P, M = map(int, sys.stdin.readline().split())
    seat = [True]+[False]*M
    no_participate = 0
    for i in range(P):
        choose = int(sys.stdin.readline())
        if seat[choose] is False:
            seat[choose] = True
        else:
            no_participate += 1
    print(no_participate)
