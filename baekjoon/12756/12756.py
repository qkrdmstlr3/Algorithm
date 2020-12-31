"""
    Author : ParkEunsik
    Date   : 2019/10/01
    url    : https://www.acmicpc.net/problem/12756
"""

import sys

atkOne, lifeOne = map(int, sys.stdin.readline().split())
atkTwo, lifeTwo = map(int, sys.stdin.readline().split())
while lifeOne > 0 and lifeTwo > 0:
    lifeOne -= atkTwo
    lifeTwo -= atkOne
if lifeOne > 0:
    print("PLAYER A")
elif lifeTwo > 0:
    print("PLAYER B")
else:
    print("DRAW")
