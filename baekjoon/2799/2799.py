"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/2799
"""
import sys

M, N = map(int, sys.stdin.readline().split())
apart = []
blind = [0, 0, 0, 0, 0]
for i in range(5*M+1):
    apart.append(sys.stdin.readline())
for i in range(1, 5*M+1, 5):
    for j in range(1, 5*N+1, 5):
        cnt = 0
        if apart[i][j] == '*':
            cnt += 1
        if apart[i+1][j] == '*':
            cnt += 1
        if apart[i+2][j] == '*':
            cnt += 1
        if apart[i+3][j] == '*':
            cnt += 1
        blind[cnt] += 1
print(' '.join(map(str, blind)))
