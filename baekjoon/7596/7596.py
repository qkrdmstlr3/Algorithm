"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/7596
"""

import sys

N = int(sys.stdin.readline())
count = 1
while N:
    song = []
    for i in range(N):
        song.append(sys.stdin.readline().rstrip())
    song.sort()
    print(count)
    count += 1
    for i in song:
        print(i)
    N = int(sys.stdin.readline())
