"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/15784
"""

import sys

N, a, b = map(int, sys.stdin.readline().split())
room = []
for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
a = a-1
b = b-1
max = room[a][b]

for i in range(N):
    if room[a][i] > max:
        print("ANGRY")
        exit()
for i in range(N):
    if room[i][b] > max:
        print("ANGRY")
        exit()
print("HAPPY")
