"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10214
"""

import sys

for _ in range(int(sys.stdin.readline())):
    score = [0, 0]
    for i in range(9):
        a, b = map(int, sys.stdin.readline().split())
        score[0] += a
        score[1] += b
    if score[0] == score[1]:
        print("Draw")
    elif score[0] > score[1]:
        print("Yonsei")
    elif score[0] < score[1]:
        print("Korea")
