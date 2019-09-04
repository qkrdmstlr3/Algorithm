"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1072
    correct percentage : 19.990%
    수학적으로 접근 > 빨리푼듯
"""

import sys

x, y = map(int, sys.stdin.readline().split())
Z = int(100*y/x)
if Z >= 99:  # Z가 99일 때 승률이 100 이 될 수는 없다!!
    print(-1)
else:
    game = int((x*(Z+1)-100*y) / (99-Z))

    percentage = int(100*(y+game)/(x+game))

    while percentage <= Z:
        game += 1
        percentage = int(100*(y+game)/(x+game))
    print(game)
