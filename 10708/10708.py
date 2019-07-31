"""
    Author : ParkEunsik
    Date   : 2019/07/31
    url    : https://www.acmicpc.net/problem/10708
"""

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
score = [0]*(N)

for i in range(M):
    game = list(map(int, sys.stdin.readline().split()))
    uncorrect = 0
    for j in range(len(game)):
        if game[j] == target[i]:
            score[j] += 1
        else:
            uncorrect += 1
    score[target[i]-1] += uncorrect

for i in range(len(score)):
    print(score[i])
